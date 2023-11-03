Primero generamos el repositorio en una nueva carpeta task-en-Djando-PatriciaRisgar y un .gitignore con el siguiente contenido:

    *.pyc
    *~
    __pycache__
    myvenv
    db.sqlite3
    /static
    .DS_Store

Despues con el comando mkvirtualenv generamos nuevo entorno virtual llamado env2

Creamos un requirements.txt con contenido: Django~=3.2.10 para hacer la instalacion de Django ejecutamos en el terminal con env2: pip install -r requirements.txt

INICIAMOS NUEVO PROYECTO.

Coninuamos en la carpeta task-en-Djando-PatriciaRisgar

```bash
    django-admin startproject mysite .
```

Se genera carpeta mysite y vamos a modificar los settings:

    TIME_ZONE = 'Europe/Berlin'
    LANGUAGE_CODE = ‘es-es’
    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR / 'static'
    ALLOWED_HOSTS = ['127.0.0.1']

Comprobamos que esté enlazado con la base de datos:

    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

Desde la terminal en env2 y la carpeta task-en-Djando-PatriciaRisgar usamos:

    ```bash
        python manage.py migrate
    ```

Iniciamos el servidor:

    ```bash
        python manage.py runserver
    ```

En el navegador ponemos http://127.0.0.1:8000/ y veremos el cohete si ha seguido los pasos anteriores.

Hago pull para contunuar despues con la creacion de la app.
