from __future__ import absolute_import
from celery.schedules import crontab

BROKER_URL = 'redis://localhost:6380'
CELERY_RESULT_BACKEND = 'redis://localhost:6380'
CELERY_RESULT_PERSISTENT = False
# TimeZone
CELERY_TIMEZONE = 'UTC'
