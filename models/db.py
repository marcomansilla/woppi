# -*- coding: utf-8 -*-

db = DAL('sqlite://storage.sqlite')

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db)
crud, service, plugins = Crud(db), Service(), PluginManager()

db.define_table(
        auth.settings.table_user_name,
        Field('first_name', length=128),
        Field('last_name', length=128),
        Field('dni'),
        Field('f_nac'),
        Field('sexo', requires=IS_IN_SET(SEXO)),
        Field('trato',requires=IS_IN_SET(TRATO)),
        Field('especialidad',requires=IS_IN_SET(ESPECIALIDADES)),
        Field('email', length=128, default='', unique=True), # required
        Field('password', 'password', length=512, readable=False, label='Password'),
        Field('direccion'),
        Field('ciudad'),
        Field('cp'),
        Field('telefono'),
        Field('celular'),
        Field('ocupacion'),
        Field('f_alta'),
        Field('registration_key', length=512, writable=False, readable=False, default=''),
        Field('reset_password_key', length=512, writable=False, readable=False, default=''),
        Field('registration_id', length=512, writable=False, readable=False, default=''),
        format = '%(trato)s, %(nombre)s, %(apellido)s'
)


## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail=auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

# Uncomment this line to disable registration
# auth.settings.actions_disabled.append('register')

# prevent massive group creation on registration
auth.settings.create_user_groups = False

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.rpx_account import use_janrain
use_janrain(auth,filename='private/janrain.key')

## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
