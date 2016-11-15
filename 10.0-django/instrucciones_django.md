Intro a django, primeros pasos:

Saber que version de django esta instalada:
```
[12:55:14@]$ python3.5 -m django --version
```

Remover viejas versiones de django:

Conocer path:
```
[12:55:14@]$python3.5 -c "import django; print(django.__path__)"
```

Si no está instalado nos bajamos los modulos de django via pip:
```
[12:55:14@]$ sudo python3.5 -m pip install django
```

Verificamos la instalación y versión de django `[12:55:14@]$python3.5`:
```
>>> import django
>>> print(django.get_version())
1.10.1
```

Crear proyecto django (crea estructuras)
```
django-admin startproject lucasweb
```

Si tienen problemas con ejecutar django-admin:
1. Buscan el path de python para la version de python que esten ejecutando.
2. dentro de ese path tiene que existir la carpeta "bin"

Luego, desde allí, por ejemplo:
```
python3.5 /Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/django/bin/django-admin.py startproject lucasweb
```

Se genera la siguiente estructura de proyecto:
```
lucasweb/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

Ejecutando la web:

```
[12:55:14@]$ python3.5 manage.py runserver
Performing system checks...
System check identified no issues (0 silenced).
You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
September 25, 2016 - 15:56:52
Django version 1.10.1, using settings 'lucasweb.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Luego, podemos chequear que nuestra web está funcionando en: http://localhost:8000/ que es lo mismo que http://127.0.0.1:8000/

Otras configuraciones de ip-puerto en el servidor local:
python3.5 manage.py runserver 0.0.0.0:8000

[Django tutorial](https://docs.djangoproject.com/en/1.10/intro/tutorial01/)
[Django, verificando errores](https://docs.djangoproject.com/en/1.10/faq/troubleshooting/#troubleshooting-django-admin)


¿Cuál es la diferencia entre un proyecto y una aplicación? Una app es una aplicación web que hace algo, por ejemplo, un sistema de blog, una base de datos de registros públicos o una aplicación de encuesta simple. Un proyecto es un conjunto de configuraciones y aplicaciones para un sitio web determinado. Un proyecto puede contener aplicaciones múltiples. Una aplicación puede estar en varios proyectos.


Crear App:

```
[12:55:14@]$ python3.5 manage.py startapp miapp
```

Estructura:

```
miapp/
  __init__.py
  apps.py
  models.py
  views.py
  admin.py
  tests.py
  migrations/
    __init__.py  
```


1. Se agrega en miapp/views.py una función que retorne un HTTP response.
from django.http import HttpResponse

```
def index(request):
    return HttpResponse("yolo!!!")
```

2. Se agrega en `miapp/urls.py`

```
from django.conf.urls import url
from django.contrib import admin
from . import views #Estoy importando a que funcion llamar.
urlpatterns = [
    url(r'^$', views.index, name='index'), #Patron de macheo para llamar a mi funcion llamada index.
]

```

Buenisimo! ya tenes tu primera app, podes correrla desde Clases-Python-101/10.0-django/djangoWeb/lucasweb$ python3.5 manage.py runserver 0.0.0.0:8000




Es probable que te de este mensaje sobre las migraciones.

```
Clases-Python-101/10.0-django/djangoWeb/lucasweb$ python3.5 manage.py runserver 0.0.0.0:8000
Performing system checks...

System check identified no issues (0 silenced).

You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
```

https://docs.djangoproject.com/es/1.10/intro/tutorial02/

Ver:
/Clases-Python-101/10.0-django/djangoWeb/lucasweb/lucasweb/settings.py

```
# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
Como se puede ver, la configuración de la base de datos está generada para poder utilizar sqlite3.
Sin embargo, estos cambios no se harán efectivos hasta que no "migremos" a nuestra base de datos.

```
Clases-Python-101/10.0-django/djangoWeb/lucasweb$ python3.5 manage.py migrate
```

Creamos el superUser.
```
Clases-Python-101/10.0-django/djangoWeb/lucasweb$ python3.5 manage.py createsuperuser
Username: admin
Email address: admin@admin.com
Password:
Password (again):
Superuser created successfully.
```


Agregando modelos:

10.0-django/djangoWeb/lucasweb/miapp/models.py


```
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

```

```
INSTALLED_APPS = [
    'miapp.apps.MiappConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

```

python3.5 manage.py makemigrations miapp

Al ejecutar makemigrations, usted le indica a Django que ha realizado algunos cambios a sus modelos (en este caso, ha realizado cambios nuevos) y que le gustaría que los guarde como una migración.

Django guarda los cambios en sus modelos como migraciones (y por lo tanto en su esquema de base de datos); son solo archivos en el disco. Usted puede leer la migración para su nuevo modelo si lo desea, es el archivo polls/migrations/0001_initial.py. No se preocupe, no se espera que usted las lea cada vez que Django hace una, sino que están diseñadas para que sean editables en caso de que usted desee modificar manualmente como Django cambia las cosas.

Hay un comando que ejecutará las migraciones para usted y gestionará el esquema de base de datos automáticamente; este se denomina migrate, y hablaremos de ello en un momento, pero primero, vamos a ver cuál SQL esa migración ejecutaría . El comando sqlmigrate recibe nombres de migración y devuelve su SQL:

python3.5 manage.py sqlmigrate miapp 0001

```
Clases-Python-101/10.0-django/djangoWeb/lucasweb$ python3.5 manage.py sqlmigrate miapp 0001
BEGIN;
--
-- Create model Choice
--
CREATE TABLE "miapp_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL);
--
-- Create model Question
--
CREATE TABLE "miapp_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "question_text" varchar(200) NOT NULL, "pub_date" datetime NOT NULL);
--
-- Add field question to choice
--
ALTER TABLE "miapp_choice" RENAME TO "miapp_choice__old";
CREATE TABLE "miapp_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL, "question_id" integer NOT NULL REFERENCES "miapp_question" ("id"));
INSERT INTO "miapp_choice" ("votes", "choice_text", "id", "question_id") SELECT "votes", "choice_text", "id", NULL FROM "miapp_choice__old";
DROP TABLE "miapp_choice__old";
CREATE INDEX "miapp_choice_7aa0f6ee" ON "miapp_choice" ("question_id");
COMMIT;
```

La salida exacta variará dependiendo de la base de datos que esté utilizando. El ejemplo anterior se genera para sqlite.

Los nombres de las tablas se generan automáticamente combinando el nombre de la aplicación (miapp) y el nombre del modelo en minúscula; question y choice. (Usted puede anular este comportamiento).

Las claves primarias (IDs) se agregan automáticamente. (Usted también puede anular esto).

Convencionalmente, Django añade "id" al nombre del campo de la clave externa ( sí, usted también puede anular esto).

La relación de la clave externa se hace explícita por una restricción``FOREIGN KEY``. No se preocupe por las partes “DEFERRABLE”; eso solo le indica a PostgreSQL que no aplique la clave externa hasta el final de la transacción.

Se adapta a la base de datos que está utilizando, así que los tipos de campos específicos de la bases de datos como auto_increment (MySQL), “serial” (PostgreSQL) o integer primary key autoincrement (SQLite) se gestionan de forma automática. Lo mismo se aplica para la cita de nombres de campos, por ejemplo, el uso de comillas dobles o comillas simples.

El comando :djadmin: sqlmigrate en realidad no ejecuta la migración en su base de datos, sólo la imprime en la pantalla para que pueda ver lo que SQL Django piensa que se requiere. Es útil para comprobar lo que Django va a hacer o si usted tiene administradores de bases de datos que requieran scripts SQL para introducir cambios.

Si le interesa, usted también puede ejecutar python manage.py check; este revisa cualquier problema en su proyecto sin hacer migraciones o modificar la base de datos.

A continuación, ejecute de nuevo migrate para crear esas tablas modelos en su base de datos:

python3.5 manage.py migrate



Agregando administración de modelos via Django admin:

10.0-django/djangoWeb/lucasweb/miapp/admin.py
```
from .models import Question

admin.site.register(Question)
```
