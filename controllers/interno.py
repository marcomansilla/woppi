# coding: utf8
# try something like
def index(): 
    
    form = SQLFORM.grid(db.medico, ui='jquery-ui', user_signature=False)

    return dict(form=form)

def especialidades():

    form = SQLFORM.grid(db.especialidad, ui='jquery-ui', user_signature=False)

    return dict(form=form)

def personal():

    form=SQLFORM.grid(db.personal, ui='jquery-ui', user_signature=False)

    return dict(form=form)
