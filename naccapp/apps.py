from django.apps import AppConfig
from threading import Thread


class TestThread(Thread):
    def run(self):
        from . import scrapy
        scrapy.scraper_func()

class NaccappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'naccapp'
   
    # def ready(self):
    #     TestThread().start()
