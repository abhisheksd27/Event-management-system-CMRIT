from django.contrib.auth.models import Group
from django.db import models


class Event(models.Model):
    # Event fields (we'll define these in later steps)
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    venue = models.CharField(max_length=255)
    expected_people = models.IntegerField()
    guest_names = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    estimated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.TimeField()
    poster = models.ImageField(upload_to='posters/')
    
    
    class Meta:
        permissions = [
            ("can_view_event", "Can view event"),
            ("can_edit_event", "Can edit event"),
            ("can_manage_event", "Can manage event"),
        ]
