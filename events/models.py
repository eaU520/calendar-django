import datetime

from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
DEADLINE = 'DE'
FITNESS = 'FI'
WORK = 'WO'
FUN = 'FN'
ETC = 'ET'
types=[(DEADLINE,"Deadline"), (FITNESS, "Fitness"), (WORK,"Work"), (FUN,"Fun"), (ETC,"etc.")]

class Event(models.Model):
    name = models.CharField(max_length=200)
    duration = models.FloatField(default=.5)
    location = models.CharField(max_length=300)
    description = models.CharField(max_length=2000)
    start = models.DateTimeField('date start')
    type = models.CharField(max_length=50, choices=types,default="DEADLINE")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="eventlist", null=True)
    
    def __str__(self) -> str:
        return "The {name} event starts at {start} and lasts {duration} hours".format(
            name=self.name, start=self.start, duration=self.duration)
        # f"Words words{ var1 + var2} , more words {self.data}"

    def is_coming_up(self):
        return self.event >= timezone.now()-datetime.timedelta(days=1)

    def get_absolute_url(self):
        return reverse('events:detail', kwargs={"pk": self.pk})

class Task(models.Model):
    name = models.CharField(max_length=250)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasklist", null=True)

    def get_absolute_url(self):
        return reverse('events:index')

    def __str__(self):
        return self.name + " " + self.event.name + " " + str(self.event.start)
#TODO: Login required annotation
class Note(models.Model):
    details = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="noteslist", null=True)

    def get_absolute_url(self):
        return reverse('events:index')

    def __str__(self):
        return self.details