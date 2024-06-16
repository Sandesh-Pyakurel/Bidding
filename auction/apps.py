from django.apps import AppConfig
from django_cron import CronJobManager


class AuctionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auction'
