# -*- coding: utf-8 -*-

def registro():
    form = SQLFORM(db.pacientes)

    if form.process().accepted:
        session.id=form.vars.id
        redirect(URL('ficha'))
        session.flash=T("Wait for approval please")
    elif form.errors:
        response.flash=T("Oops, something is wrong with your form")
    else:
        response.flash=T("Please fill the form")

    return dict(form=form)

def ficha():
    formf=SQLFORM(db.fichas)

    if formf.process().accepted:
        redirect(URL('default','index'))
        session.flash=T('Su solicitud esta pendiente')
    elif formf.errors:
        response.flash=T("Oops, something is wrong with your form")
    else:
        response.flash=T("Please fill the form")

    return dict(form=formf)

def turnos():
    form =SQLFORM.factory(Field('dni','integer',label='Numero de documento'))
    if form.process().accepted:
        response.flash=''
        personas=db(db.pacientes.dni==form.vars.dni).select()
        if len(personas):
            for persona in personas:
                session.paciente=persona.id
        else:
            session.flash=T('El paciente no existe')
            redirect(URL('turnos'))
        redirect(URL('cturno'))
    elif form.errors:
        response.flash=''
    else:
        response.flash=''
    return dict(form=form)

def cturno():
    form=SQLFORM(db.turnos)
    form.vars.paciente=session.paciente
    if form.process().accepted:
        response.flash=''
    elif form.errors:
        response.flash=''
    else:
        response.flash=''
    return dict(form=form)
