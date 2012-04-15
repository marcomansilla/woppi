# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = ' '.join(word.capitalize() for word in request.application.split('_'))
response.subtitle = T('Heath care system')

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Marco Mansilla  <contacto@marcomansilla.com.ar>'
response.meta.description = 'Sistema de gestion de pacientes'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'
response.meta.copyright = 'Copyright 2011'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default','index'), [])
    ]

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
    response.menu+=[
        (SPAN('Administracion',_style='color:yellow'),False, None, [
                (T('Medicos'),False,URL('woppi','interno','index')),
                (T('Especialidades'),False,URL('woppi','interno','especialidades')),
                (T('Personal'),False,URL('woppi','interno','personal')),
                (T('Community'),False, None, [
                        (T('Groups'),False,'http://www.web2py.com/examples/default/usergroups'),
                        (T('Twitter'),False,'http://twitter.com/web2py'),
                        (T('Live Chat'),False,'http://webchat.freenode.net/?channels=web2py'),
                        ]),
                (T('Plugins'),False,None, [
                        ('plugin_wiki',False,'http://web2py.com/examples/default/download'),
                        (T('Other Plugins'),False,'http://web2py.com/plugins'),
                        (T('Layout Plugins'),False,'http://web2py.com/layouts'),
                        ])
                ])
        ]
    response.menu+=[
        (SPAN('Gestion general',_style='color:yellow'),False, None, [
                (T('Pacientes'),False,URL('woppi','publico','index')),
                (T('Obras Sociales'),False,URL(app,'publico','osociales')),
                (T('Especialidades'),False,URL(app,'interno','especialidades')),
            
        ])
        

         ]
_()

