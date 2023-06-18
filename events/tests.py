from django.test import TestCase
from calendar_manager import Event
# Create your tests here.

class EventTestCase(TestCase):
    def setUp(self):
        Event.objects.create(name = "Test1-short", duration = .1, location = "Home Office", description = "Short test event", start = "2023-06-19 00:00:00+00:00",type ="DEADLINE")
        Event.objects.create(name = "Test2-long", duration = 10.5, location = "Home Office", description = "Long event for testing", start = "2023-10-31 08:00:00+00:00",type ="FITNESS")
        Event.objects.create(name = "Test3-future", duration = 1.5, location = "Home Office", description = "Short event in the future for testing", start = "2024-10-29 00:00:00+00:00",type ="FUN")
    def test_events_created(self):
        event_short = Event.objects.get(name="Test1-short")
        self.assertTrue(event_short.is_coming_up())
        event_short = Event.objects.get(name="Test1-short")
        self.assertEquals(event_short.to_str(),"The Test1-short event starts at 2023-10-29 00:00:00+00:00 and lasts .5 hours")
