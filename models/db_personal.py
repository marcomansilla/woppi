# -*- coding: utf-8 -*-
from plugin_lazy_options_widget import lazy_options_widget
from plugin_suggest_widget import suggest_widget

db.define_table('h_clinica',
    Field('paciente', db.pacientes),
    Field('medico', db.auth_user),
    Field('fecha','datetime', default=request.now),
    Field('dinostico','text')
    )

db.define_table('recetas',
    Field('paciente',db.pacientes),
    Field('medico',db.auth_user),
    Field('medicamentos','text')
    )

db.define_table('practicas',
    Field('solicitante',db.auth_user),
    Field('paciente',db.pacientes),
    Field('fecha','datetime'),
    Field('detalle','text')
    )

db.define_table('informes',
    Field('responsable',db.auth_user),
    Field('pedido',db.practicas),
    Field('fecha','datetime'),
    Field('informe','text')
    )

db.define_table('fechas',
    Field('medico',db.auth_user),
    Field('fecha','date'),
    )

db.define_table('horarios',
    Field('fecha',db.fechas),
    Field('hora_ini','time'),
    Field('hora_fin','time'),
    )

