from app.models.event_class import Event
import datetime


event1 = Event(datetime.date(2020, 1 , 12), "Staff Meeting", 35,'EDI1', "All staff meeting", True)
event2 = Event(datetime.date(2020, 1 , 18), "Staff Meeting", 35,'EDI1', "All staff meeting", True)
event3 = Event(datetime.date(2020, 1 , 14), "Staff Meeting", 35,'EDI1', "All staff meeting", False)

events = [event1, event2, event3]

def add_new_event(event):
    events.append(event)