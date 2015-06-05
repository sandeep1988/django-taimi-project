# -*- coding: utf-8 -*-
import os, sys
gettext = lambda s: s
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(PROJECT_PATH, "apps"))

try:
    from local_settings import *
except ImportError:
    pass

TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG
SEND_BROKEN_LINK_EMAILS = False

ADMINS = (
    ('Martin', 'mcote@d-modules.com'),
)

# ALLOWED_HOSTS = ['localhost', '127.0.0.1','.taimi.ca']
ALLOWED_HOSTS = []

MANAGERS = ADMINS

TIME_ZONE = 'America/Montreal'

LANGUAGE_CODE = 'en'

SITE_ID = 1

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")
MEDIA_URL = "/media/"
ADMIN_MEDIA_PREFIX="/media/admin/"

STATIC_ROOT = os.path.join(PROJECT_PATH, "static")

STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, "base_static"),
)

LOCALE_PATHS = (
    os.path.join(PROJECT_PATH, 'locale/'),
)


COMPRESS_ENABLED = False

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

SECRET_KEY = 'm5j!%pq@@2=irv5s(rl^vkcec39itvt4a#it&#_t%r+3g)k7)d'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (os.path.join(PROJECT_PATH, '../templates'),)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'sekizai.context_processors.sekizai',
    'cms.context_processors.media',
	'context_processors.client_info',
    'context_processors.myurl',
	"multilingual.context_processors.multilingual",
    
)
MIDDLEWARE_CLASSES = (
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
)

CMS_TEMPLATES = (
    ('index.html', 'Home'),
    ('about.html', 'About'),
	('content.html', 'Content'),
    ('produits.html', 'Products'),
    ('produits/produit_content.html', 'Produit content'),
	('contact.html', 'Contact'),
    ('advantages.html', 'Advantages'),
    ('nouvelles/newspage.html', 'Nouvelles'),
    ('warranty.html', 'Warranty'),
    ('catalogue_brochures.html', 'Catalogue brochures'),
    ('merci.html', 'Thanks'),
)

CMS_FLAT_URLS = True

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.admin',
	'django.contrib.redirects',
    'cms',
    'mptt',
    'menus',
    'south',
    'appmedia',
    'sekizai',
    'autoslug',
    'multilingual',
    # 'cms.plugins.text',
    # 'cms.plugins.picture',
    # 'cms.plugins.video',
    # 'cms_extended',
    # 'cms.plugins.file',
	'ckeditor',
    "compressor",
    'sorl.thumbnail',
    'crispy_forms',
    
	'nouvelles',
	'produits',
	'utilities',
    'testimonies',
    'taimi_calculator',
)

LANGUAGES = [
    ('en', 'English'),
    ('fr', u'Français'),
    ('es', u'Español'),
    ('pt', u'Português'),
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
        'height': 300,
        'width': 300,
    },
}

TINYMCE_FILEBROWSER = False
CKEDITOR_UPLOAD_PATH = PROJECT_PATH + "/media/ckupload/"
CMS_SEO_FIELDS = True

CRISPY_TEMPLATE_PACK = "bootstrap"

ES_API_KEY = "d1cf977381e2411a8c013bfea673cb4e"
ES_API_SECRET = "yiotqEYNdJcAnjllnX5DLqjkV2IWdWbgQ8g79TzhHyJ7mqTenMefNTJhOnvjwOLT"