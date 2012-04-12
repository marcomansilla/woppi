# -*- coding: utf-8 -*-

db.define_table('especialidad',
    Field('nombre'),
    format ='%(id)s - %(nombre)s'
    )

db.define_table('medico',
    Field('titulo',requires=IS_IN_SET(['Dr.','Dra.','Lic.'])),
    Field('nombre'),
    Field('apellido'),
    Field('dni','integer'),
    Field('matricula','integer'),
    Field('especialidad',db.especialidad),
    Field('domicilio'),
    Field('telefono','integer'),
    Field('celular','integer'),
    Field('comentarios','text'),
    Field('fealta','datetime',label='Fecha Alta',default=request.now,writable=False),
    format = '%(titulo)s %(apellido)s %(nombre)s'
    )

db.define_table('personal',
    Field('nombre'),
    Field('apellido'),
    Field('dni','integer'),
    Field('cargo'),
    Field('fnac','date',label='Fecha de nacimiento'),
    Field('sexo'),
    Field('domicilio'),
    Field('telefono','integer'),
    Field('celular','integer'),
    Field('comentarios','text'),
    Field('fealta','datetime',default=request.now,writable=False,label='Fecha de alta'),
    format = '%(id)s - %(apellido)s %(nombre)s'
    )
