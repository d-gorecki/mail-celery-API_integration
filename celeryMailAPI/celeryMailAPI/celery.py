import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celeryMailAPI.settings")
app: Celery = Celery("celeryMailAPI")
app.config_from_object("django.conf.settings", namespace="CELERY")


app.autodiscover_tasks()
