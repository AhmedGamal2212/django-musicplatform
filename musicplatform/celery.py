from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'musicplatform.settings')
app = Celery('musicplatform')
app.conf.enable_uts = False

app.conf.update(timezone='Africa/Cairo')
app.config_from_object(settings, namespace='CELERY_CONF')

# Celery Beat settings
app.conf.beat_schedule = {
    'send-inactivity-mail-every-day': {
        'task': 'albums.tasks.check_for_added_albums',
        'schedule': crontab(hour=0, minute=0)
    }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
