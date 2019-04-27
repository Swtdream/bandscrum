import datetime
from django.db import models
from django.utils import timezone
import django_filters

# Create your models here.
class Track(models.Model):
    trackName = models.CharField(max_length=200)
    trackVotes = models.CharField(max_length=200)
    trackStatus = models.TextField(max_length=500)
    trackNominateUser = models.TextField(max_length=200)

    def __str__(self):
        return self.trackName
