# coding: utf8
# try something like
def index(): 
    
    form = SQLFORM.smartgrid(db.paciente, ui='jquery-ui', user_signature=False)

    return dict(form=form)

def osociales():

    form = SQLFORM.smartgrid(db.osocial, ui='jquery-ui', user_signature=False)

    return dict(form=form)
