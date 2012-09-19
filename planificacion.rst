.. header::
     
     Marco Mansilla 

     Instituto Maria del Rosario de San Nicolas
.. footer::

      Final de Seminario de sistemas

      Pagina ###Page### 
      

========================
Descripcion del proyecto
========================

Presentacion
------------

Woppi es un sistema de gestion de especialidades medicas, concebido con el concepto basico de integracion optima de tareas mediante la asignacion de roles a los usuarios.

Las caracteristicas ofrecidas estan pensadas en la practicidad del sistema para administrar actividades y ofrecer informacion en tiempo real:

    * Gestion de Usuarios
    * Asignacion de roles
    * Gestion de Especialidades
    * Gestion de Turnos
    * Pedidos de estudios
    * Notificaciones varias

Esta organizado de manera modular, de manera que en cualquier momento se puede prescindir de cualquiera de estos o agregar modulos personalizados.

=========
Objetivos
=========

Optimizar las transacciones entre unidad medica y los pacientes, en sus distintos niveles de complejidad y areas.

Los pacientes podran realizar tramites via web sin demora, como ser pedido de turnos, consulta de analisis e historias clinicas.

Los medicos y personal cuentan con acceso distinto tipo de informacion segun el rol que le es asignado (el sistema cuenta con una politica de Control de Accesos Basado en Roles).

=====================
Documentacion tecnica
=====================

Analisis
--------

Asesor Tecnico
-------------- 

Dra. Estela Luz Tapia

Captura de requisitos
---------------------

Encuesta:
---------

1. Que Rol cumple en esta empresa?
    Soy la jefa de ginecologia.

2. Cual es el nivel de concurrencia diario que tiene la clinica?
    En general es muy alto, en numeros generales estamos hablando de un aproximado de 700 personas a 800 personas en promedio, hay dias en las que se superan ampliamente las 1500 personas.

3. Cual es el problema puntual que tiene la organizacion?
    Hay muchos, todos tienen que ver con la gente que se encuentra en la clinica y el tiempo que les toma hacer consultas sencillas o pedir estudios terminados.

4. Actualmente de que manera esta administrada su organizacion?
    La administracion se realiza de manera manual, por medio de planillas y fichas personales, algunas consultas se realizan por medio de sistemas externos y hay una base de datos que administra la provision de medicamentos.

#. Cree que una sistematizacion de la gestion de informacion de su empresa ayudaria a tener un mejor una mejor orgazacion y control?
    Si, definitivamente. Estamos conscientes del avance tecnologico y la intencion es aprovechar estas ventajas para optimizar nuestra forma de trabajo.

#. Que factores limitan a la instroduccion de nuevas tecnologias a su empresa?
    Nos resulta limitante la falta de conocimiento del personal, lo cual con el incentivo apropiado podriamos superar, y la falta de infraestructura en cuanto a lo que podria requerir un sistema administrativo.

#. Que es lo que espera de nuestro sistema?
    A corto plazo esperamos que la concurrencia de pacientes por gestion de turnos o consultas irrelevantes sea minima, dado que el sistema debera ocuparse de eso, que la informacion requerida por medicos como historias clinicas y resultados de laboratorio esten disponibles de manera rapida y fiable.

#. Su personal esta capacitado en informatica?, de no ser asi, estarian dispuestos ser capacitados por nuestra empresa?
    Desconosco el nivel de conocimiento individual que puedan tener, pero estoy al tanto de que todos tienen conocimientos de informatica basica, navegacion por internet y ofimatica.

    Vamos a realizar un sondeo para ver el nivel de conocimiento individual y la predisposicion que hay por parte de quienes requieran ser capacitados para poder operar el sistema venidero.

Estudio de factibilidad o viabilidad tecnica
--------------------------------------------

Requerimientos de Hardware
--------------------------

Se requiere un servidor principal y los clientes dependeran del numero de terminales funcionales que se deseen, con los siguientes detalles:

+----------------------------------------------------------+
|               Servidor                                   |
+==================+=======================================+
|  Procesador      | Intel Pentium 4 o AMD Athlon X2 o sup |
+------------------+---------------------------------------+
|  Memeoria        | 3GB DDR2 667 o sup.                   |
+------------------+---------------------------------------+
|  Disco Duro      | 500GB 7200RPM o sup                   |
+------------------+---------------------------------------+


+----------------------------------------------------------+
|               Cliente                                    |
+==================+=======================================+
|  Procesador      | Intel Pentium 4 o AMD Athlon X2 o sup |
+------------------+---------------------------------------+
|  Memeoria        | 512MB DDR400 o sup.                   |
+------------------+---------------------------------------+
|  Disco Duro      | 80GB 7200RPM o sup                    |
+------------------+---------------------------------------+

Se recomienda el uso de UPS en los puestos de trabajo para asegurar el buen funcionamiento del servicio.

Requerimientos de Software
--------------------------

+-----------------------------------------------------------+
|               Servidor                                    |
+===================+=======================================+
|  Sistema Operativo| MS Windows, GNU/Linux, MacOS o BSD    |
+-------------------+---------------------------------------+
|  Base de datos    | MySQL, PostgreSQL, Firebird o MongoDB |
+-------------------+---------------------------------------+
|  Servidor web     | Apache                                |
+-------------------+---------------------------------------+
|  Aplicaciones     | Python > 2.4, reportlab               |
+-------------------+---------------------------------------+

+-----------------------------------------------------------+
|               Cliente                                     |
+===================+=======================================+
|  Sistema Operativo| MS Windows, GNU/Linux, MacOS o BSD    |
+-------------------+---------------------------------------+
|  Navegador web    | Mozilla Firefox, Chrome, Opera        |
+-------------------+---------------------------------------+
|  Ofimatica        | LibreOffice, Okular (pdf)             |
+-------------------+---------------------------------------+

Al ser un sistema multiplataforma los requisitos en cuanto a software son muy flexibles y con la opcion de software libre es mucho mas variado el abanico de posibilidades en cuando a sistemas operativos para cliente/servidor, ademas de las aplicaciones necesarias para el correcto funcionamiento del sistema. 

Requerimientos de Telecomunicaciones
------------------------------------

Es necesario contar con una red local de 100 Mbit/s (se recomienda 1000 Mbit/s), que interconecte a los clientes que se encuentran en las estaciones de trabajo con el servidor principal.

La red local (LAN), puede ser cableada utilizando un router y un swtich como minimo o puede implementarse de manera inalambrica (WIFI), si se desea que clientes externos a la LAN puedan hacer consultas en el servidor, se requerira una conexion a internet con una velocidad de subida de 512kb.

Ademas de los clientes estaticos, existe la posibilidad de utilizar el sistema web mediante dispositivos moviles que cuenten con una conexion a internet y un navegador web.

Estudio de factibilidad o viabilidad operativa
----------------------------------------------

* La implementacion de sistema de hara una vez que este este terminado.

* Se va a capacitar a los operarios del sistema y a los medicos que lo vayan a utilizar.

* Se soporta el sistema completo por 3 meses

* Las tareas listadas estan bonificadas dentro del presupuesto final.

Estudio de factibilidad o viabilidad legal
------------------------------------------

* Este software esta liberado bajo las condiciones de la Licencia Publica General, lease licencia.txt

* La informacion fiscal homologada para facturacion se realizara a pedido del cliente y por separado del presente presupuesto.

* Los modulos fiscales son desarrollados a medida por marca y modelo de impresora asi como la regulacion fiscal correspondiente segun la categoria tributaria del cliente.

Detalle de costos
-----------------

+----------------------------+------------------------+
| Detalle                    | Costo                  |
+============================+========================+
| Consulta                   | Bonificada             |
+----------------------------+------------------------+
| Analisis de requerimiento  | $300,00                |
+----------------------------+------------------------+
| Desarrollo del sistema     | $9000,00               |
+----------------------------+------------------------+
| Software requerido         | Software Libre         |
+----------------------------+------------------------+
| Hardware requerido         | $1500,00               |
+----------------------------+------------------------+
| Instalacion de software    | $400,00                |
+----------------------------+------------------------+
| Mantenimiento mensual      | $300,00                |
+----------------------------+------------------------+
| Capacitacion de personal   | Bonificada             |
+----------------------------+------------------------+
| Respaldo de datos anual    | $360,00                |
+----------------------------+------------------------+
| Total                      |  $11.860,00            |
+----------------------------+------------------------+

+----------------+-----------------+-------------------+-----------------+
| Año            | Costo           | Beneficio         | Beneficio neto  |
+================+=================+===================+=================+
| **0**          | $11.860,00      |       0           |  -$11.860,00    |
+----------------+-----------------+-------------------+-----------------+
| **1**          | $3.960,00       |   $18.000,00      |   $14.040,00    |
+----------------+-----------------+-------------------+-----------------+
| **2**          | $3.960,00       |   $25.000,00      |   $21.040,00    |
+----------------+-----------------+-------------------+-----------------+
| **3**          | $3.960,00       |   $37.000,00      |   $33.040,00    |
+----------------+-----------------+-------------------+-----------------+
| **4**          | $3.960,00       |   $49.000,00      |   $45.040,00    |
+----------------+-----------------+-------------------+-----------------+

======================
Requisitos Funcionales
======================

* Woppi permite administrar la gestion de las tareas de cada area.

* Gestiones para los medicos
    * Consulta de pacientes
    * Historia clinica general
    * Informes de laboratorios

* Gestiones de pacientes
    * Reserva de turnos
    * Confirmacion de turnos
    * Consulta de resultados de estudios
    * Consulta de historia clinica

* Gestiones administrativas
    * Asignacion de turnos
    * Confirmacion de entrega de informes
    * Notificaciones a los medicos
    * Consultas de estado en laboratorios
    * Gestion de farmacia

=========================
Requisitos No Funcionales
=========================

* Facilitar la gestion interna y externa de la clinica.

* Poder acceder desde distintos dispositivos (pc, tablet, notebook, smartphone, etc.), y desde distintos sistemas operativos (MS Windows*, GNU/Linux, MacOS, BSD, etc.)


==================================
Modelado de requisitos funcionales
==================================

Identificacion de actores
-------------------------

* Medico
    Se encarga de dar realizar y confirmar los turnos de consulta, historias clinicas y solicitar resultados de estudios para su posterior evaluacion.

* Paciente
    Solicita turnos de consulta, se realiza los estudios en laboratorio, gestiona medicamentos prescriptos.

* Administrativo/Usuario de sistema
    Toma los turnos, da alta a los pacientes, consulta turnos disponibles, cancela turnos, gestiona informacion de laboratorio.

* Administrador de sistemas
    Quien se encarga de gestiones globales, de asignar nuevos roles a medicos, usuarios de sistema y pacientes de ser requerido.

* Soporte tecnico
    Personal que se ocupa de tareas de mantenimiento o soporte en caso de fallas generales relacionadas con hardware, estos deben ser guiados por el administrador en caso de fallas de software, dado que es quien mejor conoce la estructura y funcionamiento del sistema.

Historial de usuario
--------------------

+---------------------------------------------------+------------------+
|                                                   | Historia #:      |
| ALTA DE PACIENTES                                 |  1               |
+=======================+==============+============+==================+
| TEST DE ACEPTACION    | Prioridad:   | Riesgo:    | Tiempo estimado: |
|                       |  1           |            |                  |
+-----------------------+--------------+------------+------------------+
| **Descripcion**                                                      |
|                                                                      |
|   El formulario de alta de pacientes , se encuentra en la seccion de |
|   altas del sitio web, una vez registrado debera autenticarse en el  |
|   formulario de acceso, entonces podra consultar sus turnos, historia|
|   clinica, solicitar turnos nuevos, etc.                             |
+----------------------------------------------------------------------+

+---------------------------------------------------+------------------+
|                                                   | Historia #:      |
| SOLICITUD DE TURNO                                |  2               |
+=======================+==============+============+==================+
| TEST DE ACEPTACION    | Prioridad:   | Riesgo:    | Tiempo estimado: |
|                       |  1           |            |                  |
+-----------------------+--------------+------------+------------------+
| **Descripcion**                                                      |
|                                                                      |
|   El paciente crea una ficha con sus datos, la cual debe ser aprobada|
|   por una secretaria o el administrador, a su vez llena una ficha con|
|   informacion de sus estado de salud a modo de historial para los    |
|   casos que se requieran.                                            |
+----------------------------------------------------------------------+

+---------------------------------------------------+------------------+
|                                                   | Historia #:      |
| INFORMES DE LABORATORIO                           |  3               |
+=======================+==============+============+==================+
| TEST DE ACEPTACION    | Prioridad:   | Riesgo:    | Tiempo estimado: |
|                       |  1           |            |                  |
+-----------------------+--------------+------------+------------------+
| **Descripcion**                                                      |
|                                                                      |
|   Los informes de estudios realizados en los laboratorios de la clini|
|   a se podran consultar por medio del sistema. Los usuarios con el ro|
|   l de medicos podran realizar estas consultas.                      |   
+----------------------------------------------------------------------+

+---------------------------------------------------+------------------+
|                                                   | Historia #:      |
| ASIGNACION DE ROLES                               |  4               |
+=======================+==============+============+==================+
| TEST DE ACEPTACION    | Prioridad:   | Riesgo:    | Tiempo estimado: |
|                       |  1           |            |                  |
+-----------------------+--------------+------------+------------------+
| **Descripcion**                                                      |
|                                                                      |
|   El usuario con privilegios de administracion que es el primero que |
|   se crea es capaz de asignar los roles a los usuarios, basandose en |
|   estos roles el sistema es capaz de reconocer a los usuarios a las  |
|   vistas, creacion y modificacion que ellos estan autorizados.       |
+----------------------------------------------------------------------+

+---------------------------------------------------+------------------+
|                                                   | Historia #:      |
| SOLICITUD DE TURNOS                               |  5               |
+=======================+==============+============+==================+
| TEST DE ACEPTACION    | Prioridad:   | Riesgo:    | Tiempo estimado: |
|                       |  1           |            |                  |
+-----------------------+--------------+------------+------------------+
| **Descripcion**                                                      |
|                                                                      |
|   El paciente luego de haber completado sus datos en el formulario de|
|   registro puede acceder a solicitar turno para lo cual debe escribir|
|   su numero de documento, el cual luego de ser verificado le solicita|
|   seleccionar especialidades, medicos, hora y fecha para ello.       |
+----------------------------------------------------------------------+

+---------------------------------------------------+------------------+
|                                                   | Historia #:      |
| ALTA DE PERSONAL                                  |  6               |
+=======================+==============+============+==================+
| TEST DE ACEPTACION    | Prioridad:   | Riesgo:    | Tiempo estimado: |
|                       |  1           |            |                  |
+-----------------------+--------------+------------+------------------+
| **Descripcion**                                                      |
|                                                                      |
|   El personal de la institucion debe solictar los accesos necesarios |
|   al usuario administrador, quien ademas le otorgara los persmisos y |
|   grupos correspondientes para que pueda desarrollar sus tareas.     |
+----------------------------------------------------------------------+



Casos de prueba
---------------

+----------------------------------------------------------------------+
|                                                                      |
| **CASO DE PRUEBA DE ACEPTACION**                                     |
+=======================+==============================================+
| CODIGO:               | **Historial de usuario:**                    |
|  01                   |  01 -  Validacion de usuario                 |
+-----------------------+----------------------------------------------+
| **Nombre:**                                                          |
|  Alta de paciente                                                    |
|                                                                      |
+----------------------------------------------------------------------+
| **Prueba**                                                           |
| El formulario de alta de paciente debe ser completado y validado     |
| antes de que este pueda ser registrado en el sistema.                |
+----------------------------------------------------------------------+
| **Entrada**                                                          |
| Los campos son validados automaticamente desde el cliente, el unico  |
| requisito para los pacientes es que su dni debe ser unico en la base |
| de datos                                                             |
+----------------------------------------------------------------------+
| **Resultado Esperado**                                               |
| Notificacion de errores el los campos que no sean validos.           |
|                                                                      |
+----------------------------------------------------------------------+
| **Evaluacion de la prueba**                                          |
| OK                                                                   |
|                                                                      |
+----------------------------------------------------------------------+

+----------------------------------------------------------------------+
|                                                                      |
| **CASO DE PRUEBA DE ACEPTACION**                                     |
+=======================+==============================================+
| CODIGO:               | **Historial de usuario:**                    |
|  02                   |  02 -  Alta de tuno                          |
+-----------------------+----------------------------------------------+
| **Nombre:**                                                          |
|  Validacion de turnos                                                |
|                                                                      |
+----------------------------------------------------------------------+
| **Prueba**                                                           |
| El formulario de alta de turno debe ser completado luego de que el   |
| dni del paciente es validado en la base de datos.                    |
+----------------------------------------------------------------------+
| **Entrada**                                                          |
| Campo de texto que solicita al usuario su numero de documento.       |
+----------------------------------------------------------------------+
| **Resultado Esperado**                                               |
| Redireccion al formulario de seleccion de especialidades, medicos y  |
| fechas para el turno solicitado. Si el dni no existe se solicita al  |
| usuario registrarse en el sistema para que este le sea otorgado.     |
+----------------------------------------------------------------------+
| **Evaluacion de la prueba**                                          |
| OK                                                                   |
|                                                                      |
+----------------------------------------------------------------------+

+----------------------------------------------------------------------+
|                                                                      |
| **CASO DE PRUEBA DE ACEPTACION**                                     |
+=======================+==============================================+
| CODIGO:               | **Atencion de consultas**                    |
|  03                   |  03 -  atencion de consultas por los medicos |
+-----------------------+----------------------------------------------+
| **Nombre:**                                                          |
|  Atencion de consultas                                               |
|                                                                      |
+----------------------------------------------------------------------+
| **Prueba**                                                           |
| El medico puede ver los turnos pendientes para el dia segun su       |
| especialidad luego de haberse logueado en el sistema.                |
+----------------------------------------------------------------------+
| **Entrada**                                                          |
| El medico se loguea en el sistema con su direccion de mail y clave   |
| el sistema lo autoriza a ver los controladores segun el grupo al que |
| pertenece.                                                           |
+----------------------------------------------------------------------+
| **Resultado Esperado**                                               |
| Listado de pacientes para la consulta del dia, estos estan por orden |
| de solicitud de turno y elazados a sus historias clinicas e informes.|
+----------------------------------------------------------------------+
| **Evaluacion de la prueba**                                          |
| OK                                                                   |
|                                                                      |
+----------------------------------------------------------------------+

+----------------------------------------------------------------------+
|                                                                      |
| **CASO DE PRUEBA DE ACEPTACION**                                     |
+=======================+==============================================+
| CODIGO:               | **Historial de medico:**                     |
|  04                   |  04 -  Historia clinica                      |
+-----------------------+----------------------------------------------+
| **Nombre:**                                                          |
|  Consulta/agregado de historia clinica                               |
|                                                                      |
+----------------------------------------------------------------------+
| **Prueba**                                                           |
| El medico consulta la informacion del usuario y su historia clinica  |
| durante su visita, este completa una nueva historia con los datos de |
| su ultima visita para que estos esten asentados en la proxima visita.|
+----------------------------------------------------------------------+
| **Entrada**                                                          |
| El nombre del paciente que asiste a la consulta esta enlazado a la   |
| historia clinica y dentro tiene la opcion de agregar una nueva visita|
+----------------------------------------------------------------------+
| **Resultado Esperado**                                               |
| Las historias clinicas deben estar disponibles para lectura y        |
| escritura por el medico que atiende al paciente durante la visita.   |
+----------------------------------------------------------------------+
| **Evaluacion de la prueba**                                          |
| OK                                                                   |
|                                                                      |
+----------------------------------------------------------------------+

==================================
Modelado de requisitos Funcionales
==================================

Tarjetas de tarea
-----------------

+---------------------------------------------------------------------------+
| **Alta de usuario**                                                       |
+===========================================================================+
| El administrador da el alta a los usuarios que requieren privilegios para |
| operar en el sistema, medicos, tecnicos, secretaria, etc.                 |
|                                                                           |
|                                                                           |
|                                                                           |
|                                                                           |
+---------------------------------------------------------------------------+

+---------------------------------------------------------------------------+
| **Consulta de turnos**                                                    |
+===========================================================================+
| Secretarias y medicos pueden consultar los turnos pendientes y terminados |
| filtrando por fecha, pacientes, especialidades, etc.                      |
|                                                                           |
|                                                                           |
|                                                                           |
|                                                                           |
+---------------------------------------------------------------------------+
