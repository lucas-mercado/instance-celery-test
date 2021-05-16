from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')
# Instancio el objeto que contendra lo relacionado a celery.
# Utilice el include para que reconozca las tareas
app = Celery('proj', include=['proj.tasks'])

# Importo la config de celery
app.config_from_object('proj.celeryconfig')
