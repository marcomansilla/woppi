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

Captura de requisitos
---------------------

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

Es necesario contar con una red local, que interconecte a los clientes que se encuentran en las estaciones de trabajo con el servidor principal.

La red local (LAN), puede ser cableada utilizando un router y un swtich como minimo o puede implementarse de manera inalambrica (WIFI), si se desea que clientes externos a la LAN puedan hacer consultas en el servidor, se requerira una conexion a internet.

Ademas de los clientes estaticos, existe la posibilidad de utilizar el sistema web mediante dispositivos moviles que cuenten con una conexion a internet y un navegador web.

Estudio de factibilidad o viabilidad operativa
----------------------------------------------

Estudio de factibilidad o viabilidad legal
------------------------------------------

Este software esta liberado bajo las condiciones de la Licencia Publica General, lease licencia.txt

Detalle de costos
-----------------

======================
Requisitos Funcionales
======================

=========================
Requisitos No Funcionales
=========================

Modelado de requisitos funcionales
----------------------------------

Identificacion de actores
-------------------------

Historial de usuario
--------------------

Casos de prueba
---------------

Modelado de requisitos Funcionales
----------------------------------

Tarjetas de tarea
-----------------


