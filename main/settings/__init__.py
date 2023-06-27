from decouple import config

ENVIRONMENT = config('ENV')

if ENVIRONMENT == 'dev':
    from .development import *
else:
    from .production import *