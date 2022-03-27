# from __future__ import absolute_import, unicode_literals
import os
import logging
from celery import Celery
from django.conf import settings

logger = logging.getLogger("Celery")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cotacao.settings")
celery = Celery("cotacao")
celery.config_from_object("django.conf:settings", namespace="CELERY")
celery.autodiscover_tasks()

