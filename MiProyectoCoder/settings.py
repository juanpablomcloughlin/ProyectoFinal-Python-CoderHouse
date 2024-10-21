from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-5#69yfv%6a$8szorhzgn5cc*#cm)rm!5$b9k3pytcjls$pk$ya'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Cambia a True en desarrollo.

# Allow all hosts during development, restrict in production
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'tu-dominio.com']  # Agrega aquí tu dominio o IP pública en producción.

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fulanos',  # Asegúrate de que esta app esté correctamente registrada.
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MiProyectoCoder.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'fulanos', 'templates')],  # O cambia a 'templates' global.
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MiProyectoCoder.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'  # Puedes cambiar esto a 'es-es' si es un proyecto en español.
TIME_ZONE = 'UTC'  # O cambia a tu zona horaria, como 'America/Argentina/Buenos_Aires'.
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# En desarrollo, usas archivos estáticos desde la carpeta 'static'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Asegúrate de que esta carpeta exista y tenga tus archivos estáticos.
]

# En producción, usa el comando collectstatic para recopilar todos los archivos en STATIC_ROOT.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Donde Django recopilará los archivos estáticos.

# Media files (subidos por los usuarios)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Carpeta donde se almacenarán los archivos subidos.

# Redirección para usuarios no autenticados
LOGIN_URL = '/fulanos/login/'  # Ajusta según la ruta de tu vista de login.

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
