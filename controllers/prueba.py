# -*- coding: utf-8 -*-

def index():
    return dict()

def alta():
    return XML("something should come up")

def form():
        if request.args(0) in db.tables:
            response.generic_patterns = ['load']
            return dict(form=SQLFORM(db[request.args(0)]).process())
        else:
            raise HTTP(404)
            
