import os
import json
import dj_database_url

SECRET_KEY = 'wa9g_mf%mrairp7#c#&&5pt0y4+5pk2skbizk!$c5km5lbzs^&'

DEBUG = False

import dj_database_url
DATABASES['default'] = dj_database_url.config('sqlite:////{0}'.format(os.path.join(BASE_DIR, 'db.sqlite3'))

DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
DATABASES['default']['NAME'] = 'movie'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

"""
connection = dj_database_url.parse(os.environ.get("DATABASE_URL"))
connection.update({
    'CONN_MAX_AGE': 600,
})
DATABASES = {
    "default": connection,
}
"""
ALLOWED_HOSTS = [os.environ.get("HOST", "*"), ]
