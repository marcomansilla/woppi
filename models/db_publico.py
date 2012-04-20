# -*- coding: utf-8 -*-

db.define_table('pedido',
    Field('paciente',db.paciente),
    Field('msolicitante',db.medico),
    Field('mpracticante',db.medico),
    Field('pedido','text'),
    Field('fecha','date')
    )

db.define_table('turno',
    Field('paciente',db.paciente),
    Field('fecha','date'),
    Field('medico',db.medico),
    Field('comentario','text')
    )

db.define_table('historia',
    Field('paciente',db.paciente),
    Field('medico',db.medico),
    Field('fecha','datetime',default=request.now),
    Field('historia','text')
    )
