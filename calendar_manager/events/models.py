import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
DEADLINE = 'DE'
FITNESS = 'FI'
WORK = 'WO'
FUN = 'FN'
types=[(DEADLINE,"Deadline"), (FITNESS, "Fitness"), (WORK,"Work"), (FUN,"Fun")]

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_duration = models.FloatField(default=.5)
    event_location = models.CharField(max_length=300)
    event_description = models.CharField(max_length=2000)
    event_start = models.DateTimeField('date start')
    event_type = models.CharField(max_length=50, choices=types,default="DEADLINE")

    def __str__(self) -> str:
        return "The {name} event starts at {start} and lasts {duration} hours".format(
            name=self.event_name, start=self.event_start, duration=self.event_duration)
        # f"Words words{ var1 + var2} , more words {self.data}"

    def is_coming_up(self):
        return self.event_start >= timezone.now()-datetime.timedelta(days=1)
