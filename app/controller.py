from flask import render_template, request
from app import app
from app.models.event_class import Event
from app.models.event_list import events, add_new_event


@app.route('/')
def index():
    #return "hello world"
    return render_template('index.html', title ='Home ', events = events)

@app.route('/add-event', methods = ['POST'])
def add_event():
    event_date = request.form["date"]
    event_name = request.form["name"]
    event_desc = request.form['description']
    event_location = request.form["room_location"]
    num_guest = request.form["number_of_guests"]
    recurring = True if "recurring" in request.form else False
    new_event = Event(event_date, event_name, event_desc, event_location, num_guest, recurring )
    add_new_event(new_event)
    return render_template('index.html', title = 'Home', events = events)
    