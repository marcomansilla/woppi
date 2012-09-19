# -*- coding: utf-8 -*-
import datetime
from plugin_hradio_widget import hradio_widget

db.define_table('pacientes',
        Field('nombre', length=128),
        Field('apellido', length=128),
        Field('dni','integer', unique=True),
        Field('f_nac','date'),
        Field('trato',requires=IS_IN_SET(TRATO_P)),
        Field('email', length=128, unique=True),
        Field('direccion','string', length=30),
        Field('ciudad','string', length=30),
        Field('cp',length=8),
        Field('telefono','integer'),
        Field('celular','integer'),
        Field('ocupacion', requires=IS_IN_SET(OCUPACION)),
        Field('f_alta', 'datetime', default=request.now, readable=False, writable=False, label=T('Fecha de Alta')),
        Field('activo','boolean', readable=False, writable=False),
        format = '%(trato)s, %(nombre)s, %(apellido)s'
    )

db.define_table('fichas',
        Field('paciente', db.pacientes, default=session.id),
        Field('sexo', requires=IS_IN_SET(SEXO)),
        Field('ecivil',requires=IS_IN_SET(ESTADO_CIVIL)),
        Field('conyugue'),
        Field('alergia_med','boolean'),
        Field('al_descripcion','text'),
        Field('enfermedad_cronica','boolean'),
        Field('en_descripcion','text'),
        Field('operacion','boolean'),
        Field('op_descripcion','text'),
        Field('medicamento','boolean'),
        Field('me_descripcion','text'),
        Field('dieta','boolean'),
        Field('sgrupo',requires=IS_IN_SET(GRUPOS)),
        Field('sfactor', requires=IS_IN_SET(FACTORES)),
        Field('fuma','boolean'),
    )

db.define_table('turnos',
        Field('paciente', db.pacientes, default=session.paciente),
        Field('especialidad', requires=IS_IN_SET(ESPECIALIDADES)),
        Field('medico',),
        Field('fecha', 'date', default=request.now),
        Field('turno'),
        Field('f_pedido','datetime')
    )

# Validadores Paciente
db.pacientes.nombre.requires=IS_NOT_EMPTY()
db.pacientes.apellido.requires=IS_NOT_EMPTY()
db.pacientes.dni.label=T('Número de DNI')
db.pacientes.email.label=T('E-Mail')
db.pacientes.cp.label=T('Codigo Postal')
db.pacientes.f_nac.label=T('Fecha de nacimiento')
db.pacientes.telefono.requires=IS_NOT_EMPTY()

# Comentarios
db.pacientes.nombre.comment=T('(obligatorio)')
db.pacientes.apellido.comment=T('(obligatorio)')
db.pacientes.dni.comment=T('(obligatorio)')
db.pacientes.trato.comment=T('(obligatorio)')
db.pacientes.email.comment=T('(obligatorio)')
db.pacientes.ocupacion.comment=T('(obligatorio)')
db.pacientes.telefono.comment=T('(obligatorio)')

# Validadores Ficha
db.fichas.sexo.label=T('Indique su sexo')
db.fichas.ecivil.label=T('Estado civil')
db.fichas.conyugue.labe=T('Nombre del conyugue')
db.fichas.alergia_med.label=T('¿Tiene alergia a algún medicamento?')
db.fichas.al_descripcion.label=T('Indique los medicamentos a los cuales es alergico')
db.fichas.enfermedad_cronica.label=T('¿Padece alguna enfermedad cronica?')
db.fichas.en_descripcion.label=T('Indique la enfermedad que padece')
db.fichas.operacion.label=T('¿Le han realizado alguna cirugia?')
db.fichas.op_descripcion.label=T('Indique que cirugia/s le han sido realizadas')
db.fichas.dieta.label=T('¿Sigue algun regimen o dieta?')
db.fichas.medicamento.label=T('¿Toma alguna medicacion?')
db.fichas.me_descripcion.label=T('Indique la medicacion que toma')
db.fichas.sgrupo.label=T('Grupo Sanguineo')
db.fichas.sfactor.label=T('Factor Sanguineo')
db.fichas.fuma.label=T('¿Fuma?')
db.fichas.conyugue.label=T('Nombre del conyugue')
db.fichas.sexo.widget=hradio_widget
db.fichas.sgrupo.widget=hradio_widget
db.fichas.sfactor.widget=hradio_widget

db.turnos.fecha.requires=requires = IS_DATE_IN_RANGE(format=T('%Y-%m-%d'),
                                                     minimum=datetime.date.today(),
                                                     maximum=datetime.date(2020,12,31),
                                                     error_message='La fecha no es correcta!')
