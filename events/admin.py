from django.contrib.auth.models import Group
from django.apps import AppConfig

class EventsConfig(AppConfig):
    name = 'events'

    def ready(self):
        Group.objects.get_or_create(name='Admin')
        Group.objects.get_or_create(name='Principal')
        Group.objects.get_or_create(name='HOD')
        Group.objects.get_or_create(name='Student')
