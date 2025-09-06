import os
from django.core.wsgi import get_wsgi_application

# Indique à Django quel fichier settings utiliser
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projet12.settings')

# Crée l'application WSGI que le serveur utilisera
application = get_wsgi_application()
