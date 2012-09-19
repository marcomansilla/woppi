#-*- coding: utf-8 -*-

def pacientes():
    form = SQLFORM.smartgrid(db.pacientes, user_signature=False)
    return dict(form=form)

def fichas():
    form = SQLFORM.smartgrid(db.fichas, user_signature=False)
    return dict(form=form)

def turnos_p():
    return dict()

def paciente():
    form = SQLFORM.factory(Field('dni','integer'))
    
    if form.process().accepted:
        response.flash=''
    elif form.errors:
        response.flash=''
    else:
        response.flash='Ingrese su DNI'

    return dict(form=form)

def turnos():
    request.vars.id=db(db.pacientes.dni==dni).select(db.pacientes.id)
    form=SQLFORM(db.turnos)
    if form.process().accepted:
        response.flash='El turno ha sido recibido'
    elif form.errors:
        response.flash='El formulario contiene errores'
    else:
        response.flash='Puede cargar su turno'

    return dict()
    
    
