#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   WebGrid for web2py 
   Developed by Nathan Freeze (Copyright 2010)
   Email <nathan@freezable.com>
   License: GPL v2
   
   This file contains code to build a table that supports
   paging, sorting, editing and totals.
   Version: 1.02
"""

from gluon.sql import Rows, Field, Set
from gluon.sqlhtml import *
from gluon.html import *
from gluon.storage import *

class WebGrid(object):    
    def __init__(self, crud, name=None, datasource=None):
        self.crud = crud
        self.environment = crud.environment
        self.name = name
        self.css_prefix = None
        self.id = None

        self.datasource = datasource
        self.crud_function = 'data'
        self.download_function = 'download'
        
        self.messages = Messages(self.crud.environment.T)
        self.messages.confirm_delete = 'Are you sure?'
        self.messages.no_records = 'No records'
        self.messages.add_link = '[add %s]'
        self.messages.edit_link = 'edit'
        self.messages.delete_link = 'delete'
        self.messages.view_link = 'view'
        self.messages.file_link = 'file'
        self.messages.page_info = 'page %(pagenum)s of %(pagecount)s (total records: %(total)s)'
        self.messages.page_total = "Total:"
        self.messages.filter = 'Filter'
        self.messages.clear_filter = 'Clear'
        self.messages.pagesize = ' pagesize: '  
        self.messages.previous_page = '<-prev '
        self.messages.next_page = ' next->'
        
        self.action_links = ['view', 'edit', 'delete']
        self.action_headers = ['view', 'edit', 'delete'] 
               
        self.field_headers = self.fields = self.totals = []     
        self.enabled_rows = ['header', 'filter', 'pager', 'totals', 
                             'footer', 'add_links']
        self.allowed_vars = ['pagesize', 'pagenum', 'sortby', 
                             'ascending', 'groupby', 'totals']
        
        self.pagenum = self.pagecount = self.pagesize = 0
        self.sortby = self.groupby = self.page_total = self.filters = None
        
        self.view_link = self.edit_link = self.delete_link = None
        self.add_links = self.action_header = None
        self.header = self.filter = self.footer = None
        self.pager = self.datarow = None
        self.pageinfo_separator = ' - '
        self.pagesizes = [10,20,30,40,50]

        self.ascending = False
        self.row_created = None
        self.filter_query = lambda field,value: field==value
        self.filter_items_query = lambda field: field['id'] > 0
        self.filter_cache = None
        self.total_function = lambda fieldvalues: sum(fieldvalues)
    
    def get_header(self, c):
        try:
            return self.field_headers[self.fields.index(c)]
        except:
            return c

    def get_value(self, f, r):
        (_t, _f) = f.split('.')
        v = r[_t][_f] if self.joined else r[_f]
        return v
    
    def update_filters(self,vrs,flt):
        if not flt:
             return
        for k, v in flt.items():
            vrs[self.name + '_filter-'+k] = v        
    
    def __call__(self):
           
        request = self.crud.environment.request
        db = self.crud.db
        datasource = self.datasource
        
        if not self.name:
            self.name = self.crud.environment.request.function
        if not self.css_prefix:
            self.css_prefix = self.name
        if not self.id:
            self.id = self.name
        
        # Set defaults
        vars = request.get_vars
        allowed = self.allowed_vars
        name = self.name
        
        if getattr(vars,name+'_pagesize') and 'pagesize' in allowed: 
            self.pagesize = int(vars[name+'_pagesize'])            
        if not self.pagesize:
            self.pagesize = 10
        
        if getattr(vars,name+'_pagenum') and 'pagenum' in allowed: 
            self.pagenum = int(vars[name+'_pagenum'])
        if not self.pagenum:
            self.pagenum = 1
        
        if getattr(vars,name+'_sortby') and 'sortby' in allowed:
            self.sortby = vars[name+'_sortby']
        
        if getattr(vars,name+'_groupby') and 'groupby' in allowed: 
            self.groupby = vars[name+'_groupby']
        
        if getattr(vars,name+'_totals') and 'totals' in allowed:
            self.totals = vars[name+'_totals']
        
        if getattr(vars,name+'_ascending') and 'ascending' in allowed:
            self.ascending = vars[name+'_ascending'] == "True"
        
        page = sortby = groupby = query = None
        filters = dict()
        
        #Build filters
        if 'filter' in self.enabled_rows:
            if not request.vars.get(name+'_clear_filter', None):
                if request.post_vars:
                    request.vars.update(request.post_vars)
                for k, v in request.vars.items():
                    if isinstance(v,list):
                        v = v[0]
                    if name + '_filter-' in k:
                        tf = k.split('-')[-1]
                        filters[tf] = v                                        
                for k, v in filters.items():
                    if v=='0': continue
                    (ft,ff) = k.split('.')
                    fld = db[ft][ff]
                    if query:
                        query &= self.filter_query(fld,v)
                    else:
                        query = self.filter_query(fld,v)
                if filters and request.vars.get(name+'_submit_filter', None):
                    request.get_vars[name+'_pagenum'] = 1              
                    self.pagenum = 1
                        
        # Build limitby
        if self.pagesize > 0:
            pagenum = self.pagenum - 1
            page = (self.pagesize * pagenum, 
                    self.pagesize * pagenum + self.pagesize)
        else: 
            self.pagenum = 0
 
        # Build sortby
        if self.sortby:
            if isinstance(self.sortby, Field):
                (ts, fs) = (self.sortby._tablename, self.sortby.name)
            else:
                (ts, fs) = self.sortby.split('.')
            if self.ascending:
                sortby = db[ts][fs]
            else:
                sortby = ~db[ts][fs]
            
        if self.groupby: 
            if isinstance(self.groupby, Field):
                (tg, fg) = (self.groupby._tablename, self.groupby.name)
            else:
                (tg, fg) = self.groupby.split('.')
            groupby = db[tg][fg]
            
        # Get rows
        rows = total = None        
        if isinstance(datasource, Rows):            
            rows = datasource
            joined = len(set(map(lambda c: c.split('.')[0], rows.colnames))) > 1            
            for k,v in filters.items():
                if v=='0': continue
                (flt_t,flt_f) = k.split('.')
                if joined:
                    rows = rows.find(lambda row: row[flt_t][flt_f]==v)
                else:
                    rows = rows.find(lambda row: row[flt_f]==v)
            total = len(rows)     
            if sortby and joined:
               rows = rows.sort(lambda row: row[ts][fs], reverse=self.ascending)
            elif sortby:
               rows = rows.sort(lambda row: row[fs], reverse=self.ascending)
            if self.pagesize > 0:
                rows = rows[page[0]:page[1]]            
        elif isinstance(datasource, Set):
            if query:
                datasource = datasource(query)
            if self.fields:
                tempids = []
                self.tablenames = list(set(map(lambda c: c.split('.')[0], 
                                               self.fields)))
                for t in self.tablenames:
                    idfield = t +'.id'                                        
                    if not idfield in self.fields:
                        self.fields.append(idfield)
                        tempids.append(idfield)
                rows = datasource.select(limitby=page, orderby=sortby, 
                                         groupby=groupby, *self.fields)
                for t in tempids:
                    self.fields.remove(t)
            else:
                rows = datasource.select(limitby=page, orderby=sortby, 
                                         groupby=groupby)
            total = datasource.count()
        elif isinstance(datasource, Table):
            rows = db(query).select(datasource.ALL, limitby=page, 
                                     orderby=sortby, groupby=groupby) 
            total = db(datasource.id > 0).count()
        elif isinstance(datasource, list) and isinstance(datasource[0], Table):
            rows = db(query).select(limitby=page, orderby=sortby, groupby=groupby,
                                    *[t.ALL for t in datasource])
            total = db(datasource[0].id > 0).count()
        else: 
            raise AttributeError("Invalid datasource for WebGrid")        
        
        self.tablenames = list(set(map(lambda c: c.split('.')[0], rows.colnames)))
        joined = len(self.tablenames) > 1        
        self.response = rows
        self.colnames = rows.colnames        
        self.joined = joined
        self.total = total
        
        if not self.fields:
            self.fields = rows.colnames
        
        if isinstance(self.fields[0], Field):
            self.fields = ['%s.%s' % (f._tablename, f.name) for f in self.fields]
            
        if self.filters and isinstance(self.filters[0],Field):
            self.filters = ['%s.%s' % (f._tablename, f.name) for f in self.filters]
            
        if self.totals and isinstance(self.totals[0], Field):
            self.totals = ['%s.%s' % (f._tablename, f.name) for f in self.totals]
            
        if not self.filters:
            self.filters = self.fields
            
        if not self.field_headers:
            self.field_headers = []
            for f in self.fields:
                (t,f) = f.split('.')
                field = db[t][f]
                if hasattr(field,'label'):
                    self.field_headers.append(field.label)
                else:
                    lbl = f.split('.')[1].replace("_", " ").capitalize()
                    self.field_headers.append(lbl)              
            
        if not self.action_headers:
            self.action_headers = self.action_links
       
        if not self.view_link and 'view' in self.action_links:            
            self.view_link = lambda row: A(self.messages.view_link, _href=self.crud.url(f=self.crud_function, 
                                                       args=['read', self.tablenames[0], 
                                                             row[self.tablenames[0]]['id'] \
                                                              if self.joined else row['id']]))          
        if not self.edit_link and 'edit' in self.action_links:             
            self.edit_link = lambda row: A(self.messages.edit_link, _href=self.crud.url(f=self.crud_function, 
                                                       args=['update', self.tablenames[0],
                                                             row[self.tablenames[0]]['id'] \
                                                              if self.joined else row['id']]))
        if not self.delete_link and 'delete' in self.action_links:            
            self.delete_link = lambda row: A(self.messages.delete_link, _href=self.crud.url(f=self.crud_function,
                                                       args=['delete', self.tablenames[0],
                                                             row[self.tablenames[0]]['id'] \
                                                              if self.joined else row['id']]),
                                                                 _onclick="return confirm('%s');" % \
                                                                    self.messages.confirm_delete)
        if not self.add_links and 'add_links' in self.enabled_rows:            
            self.add_links = lambda tables: TR(TD([A(self.messages.add_link % t,
                                                         _href=self.crud.url(f=self.crud_function, 
                                                       args=['create', t])) for t in self.tablenames],
                                                       _colspan=len(self.action_headers)+
                                                                len(self.field_headers)),
                                                                _class=self.css_prefix + '-webgrid add_links')           

        if not self.header and 'header' in self.enabled_rows:
            def header(fields):
                thead = TR([TH(c) for c in self.action_headers],
                              _class=self.css_prefix + '-webgrid header')
                for f in fields:
                    vars = dict(request.get_vars)
                    self.update_filters(vars,filters)
                    vars[name+'_pagenum'] = 1
                    vars[name+'_sortby'] = f
                    vars[name+'_ascending'] = not self.ascending
                    href = URL(r=request,vars=vars,args=request.args)
                    th = TH(A(self.get_header(f),_href=href))
                    thead.components.append(th)
                return thead
            
            self.header = header
            
        if not self.filter and 'filter' in self.enabled_rows:
            def filter(fields):
                tr = TR([TD('') for c in self.action_links],
                        _class=self.css_prefix + '-webgrid filter')
                if self.action_links:
                    submit_filter = INPUT(_type='submit',
                                                 _value=self.messages.filter,
                                                 _name=name+'_submit_filter')
                    clear_filter = INPUT(_type='submit',
                                                 _value=self.messages.clear_filter,
                                                 _name=name+'_clear_filter')
                    tr.components[-1] = TD(clear_filter,submit_filter) 
                for f in fields:
                    if not f in self.filters:
                        tr.components.append(TD(''))
                        continue
                    (tf,ff) = f.split('.')
                    curfld = db[tf][ff]
                    if curfld.type=='upload' or curfld.type=='blob':
                            continue
                    vals = db(self.filter_items_query(db[tf])).select(db[tf]['id'],curfld,
                                                     cache=self.filter_cache)
                    dval = filters.get(f)
                    prev = []
                    opts = []
                    for v in vals:
                        opt = None               
                        if curfld.type.startswith('reference '):
                            if curfld.represent:
                                rp = curfld.represent(v[ff])
                                if rp and not rp in prev:
                                    opt = OPTION(rp, _value=v[ff])
                                    prev.append(rp)
                            else:
                                v = v[ff]
                                if v and not v in prev:
                                    opt = OPTION(v,_value=v)
                                    prev.append(v)                                                                
                        elif curfld.represent:                            
                            rp = curfld.represent(v[ff])
                            if rp and not rp in prev:
                                opt = OPTION(rp, _value=rp) 
                                prev.append(rp)
                        else:
                            if v[ff] and not v[ff] in prev:
                                opt = OPTION(v[ff], _value=v[ff]) 
                                prev.append(v[ff])
                        if opt:
                            opts.append(opt)
                    opts.sort(key=lambda x: x.components[0])
                    inp = SELECT(opts, _name = name+'_filter-'+f,value=dval)
                    inp.components.insert(0,OPTION('',_value='0'))                    
                    tr.components.append(TD(inp))
                return tr
            self.filter = filter
            
        if not self.footer and 'footer' in self.enabled_rows:
            def footer(fields):                  
                pageinfo = pagesize = ''
                pagelinks = SPAN(self.messages.pagesize)
                if not self.groupby:
                    vars = dict(request.get_vars)
                    self.update_filters(vars,filters)
                    for p in self.pagesizes:
                        vars[name+'_pagesize'] = p
                        vars[name+'_pagenum'] = 1
                        lnk = A(str(p),' ',_href=URL(r=request,args=request.args,
                                                           vars=vars))
                        pagelinks.components.append(lnk)
                    pageinfo = self.messages.page_info % {'pagenum':self.pagenum,
                                                'pagecount':self.pagecount,
                                                'total':self.total}
                tr = TR(_class=self.css_prefix + '-webgrid footer')
                td = TD(pageinfo,self.pageinfo_separator,pagelinks,
                        _colspan=len(self.fields) + len(self.action_links))
                tr.components.append(td)
                return tr
            self.footer = footer
                                   
        if not self.pager and 'pager' in self.enabled_rows:
            def pager(pagecount):
                vars = dict(request.get_vars)
                self.update_filters(vars,filters)              
                prev = A(self.messages.previous_page, _href="#")
                next = A(self.messages.next_page, _href="#")
                if self.pagesize > 0 and pagenum > 0:
                    vars[name+'_pagenum'] = self.pagenum - 1
                    prev = A(B(self.messages.previous_page), 
                             _href=URL(r=request,vars=vars,args=request.args))
                if self.pagesize > 0 and self.pagenum < pagecount and \
                                len(self.response) >= self.pagesize:
                    vars[name+'_pagenum'] = self.pagenum + 1
                    next = A(B(self.messages.next_page), 
                             _href=URL(r=request,vars=vars,args=request.args))
                tr = TR(_class=self.css_prefix + '-webgrid pager')
                td = TD(prev,_colspan=len(self.fields) + len(self.action_links) )
                (p1, m1) = (pagenum - 5,'...') if pagenum > 5 else (1, '')
                (p2, m2) = (pagenum + 5,'...') if pagenum + 5 < pagecount else (pagecount, '')
                if p2 < 11: p2 = 11
                td.components.append(m1)
                for x in xrange(p1,p2):
                    if not self.groupby:
                        vars[name+'_pagenum'] = x
                        href = URL(r=request,vars=vars,args=request.args)
                        td.components.append(A(x if x <> pagenum + 1 else
                                                B(x),'-',_href=href))
                td.components.append(m2)
                td.components.append(next)
                tr.components.append(td)                
                return tr
            self.pager = pager
            
        if not self.page_total and 'totals' in self.enabled_rows:
            def page_total():
                pagetotal = TR(['' for l in self.action_links],
                               _class=self.css_prefix + '-webgrid totals')
                if self.action_links:
                    pagetotal.components[-1] = TD(self.messages.page_total)
                for f in self.fields:
                    if f in self.totals:
                        fieldvalues = [self.get_value(f, r) for r in self.response]
                        fieldtotal = self.total_function(fieldvalues) 
                        pagetotal.components.append(TD(fieldtotal)) 
                    else:
                        pagetotal.components.append(TD()) 
                return pagetotal                       
            self.page_total = page_total 
            
        if not self.action_links:
            if self.totals or self.filters:
                self.action_links = ['delete']
                self.action_headers = ['']
                self.delete_link = lambda row: ' '
          
        table_field = re.compile('[\w_]+\.[\w_]+')
        table = TABLE(_id=self.id)        
        if 'header' in self.enabled_rows:
            _row = self.header(self.fields)
            if self.row_created:
                self.row_created(_row,'header',None)
            table.components.append(THEAD(_row))
        if 'filter' in self.enabled_rows:
            _row = self.filter(self.fields)
            if self.row_created:
                self.row_created(_row,'filter',None)
            table.components.append(_row)
        if len(rows) == 0:
            table.components.append(TR(TD(self.messages.no_records,
                                       _colspan=len(self.fields) + len(self.action_links),
                                       _style="text-align:center;")))
        for (rc, row) in enumerate(rows):            
            if self.datarow:
                _row = self.datarow(row)
                if self.row_created:
                    self.row_created(_row,'datarow',row)
                table.components.append(_row)
                continue
            _class = 'even' if rc % 2 == 0 else 'odd'
            tr = TR(_class=self.css_prefix + '-webgrid-row %s' % _class) 
            if 'view' in self.action_links:
                tr.components.append(TD(self.view_link(row), 
                                        _class=self.css_prefix + '-webgrid view_link'))
            if 'edit' in self.action_links:
                tr.components.append(TD(self.edit_link(row), 
                                        _class=self.css_prefix + '-webgrid edit_link'))
            if 'delete' in self.action_links:
                tr.components.append(TD(self.delete_link(row), 
                                        _class=self.css_prefix + '-webgrid delete_link'))

            for colname in self.fields:
                if not table_field.match(colname):
                    r = row._extra[colname]
                    tr.components.append(TD(r))
                    continue
                (tablename, fieldname) = colname.split('.')
                field = rows.db[tablename][fieldname]
                r = row[tablename][fieldname] if joined else row[fieldname]
                if field.represent:
                    r = field.represent(r)
                    tr.components.append(TD(r))
                    continue
                if field.type == 'blob' and r:
                    tr.components.append(TD('DATA'))
                    continue
                r = str(field.formatter(r))
                if field.type == 'upload':
                    if r:
                        tr.components.append(TD(A(self.messages.file_link, 
                                                  _href=URL(r=self.environment.request,
                                                            f=self.download_function, args=r))))
                    else:
                        tr.components.append(TD(self.messages.file_link))
                    continue
                tr.components.append(TD(r))            
            if self.row_created:
                self.row_created(tr,'datarow',row)
            table.components.append(tr)
            
        if self.pagesize > 0:
            pagecount = int(total / self.pagesize)
            if total % self.pagesize != 0: pagecount += 1
        else:
            pagecount = 1
            
        self.pagecount = pagecount
        
        footer_wrap = TFOOT()
        if 'totals' in self.enabled_rows and len(rows):
            _row = self.page_total()
            if self.row_created:
                self.row_created(_row,'totals',None) 
            footer_wrap.components.append(_row)
        if 'add_links' in self.enabled_rows: 
            _row = self.add_links(self.tablenames)
            if self.row_created:
                self.row_created(_row,'add_links',None)
            footer_wrap.components.append(_row)        
        if 'pager' in self.enabled_rows and len(rows):
            _row = self.pager(pagecount)
            if self.row_created:
                self.row_created(_row,'pager',None)
            footer_wrap.components.append(_row)        
        if 'footer' in self.enabled_rows and len(rows): 
            _row = self.footer(self.fields)
            if self.row_created:
                self.row_created(_row,'footer',None)
            footer_wrap.components.append(_row)                    

        table.components.append(footer_wrap)
           
        return FORM(table,_class=self.css_prefix + '-webgrid',_name=name+'-webgrid-form')
