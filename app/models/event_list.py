from app.models.event_class import Event


event1 = Event("Nov 1", "Staff Meeting", 35,'EDI1', "All staff meeting")
event2 = Event("Nov 2", "Staff Meeting", 35,'EDI1', "All staff meeting")
event3 = Event("Nov 3", "Staff Meeting", 35,'EDI1', "All staff meeting")

events = [event1, event2, event3]

def add_new_event(event):
    events.append(event)