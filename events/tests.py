from django.test import TestCase
from calendar_manager import Event
# Create your tests here.

class EventTestCase(TestCase):
    def setUp(self):
        Event.objects.create(name = "Test1-short", duration = .1, location = "Home Office", description = "Short test event", start = "2023-10-29 00:00:00+00:00",type ="DEADLINE")
        Event.objects.create(name = "Test2-long", duration = 10.5, location = "Home Office", description = "Long event for testing", start = "2023-10-31 08:00:00+00:00",type ="FITNESS")
        Event.objects.create(name = "Test3-future", duration = 1.5, location = "Home Office", description = "Short event in the future for testing", start = "2024-10-29 00:00:00+00:00",type ="FUN")
)