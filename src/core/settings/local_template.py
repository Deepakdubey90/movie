
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wa9g_mf%mrairp7#c#&&5pt0y4+5pk2skbizk!$c5km5lbzs^&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'vss',
    }
}
