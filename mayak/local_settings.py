from .settings import *

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': '/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map', r'.+\node_modules']
    }
}

APP_VERSION = 1.0

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
