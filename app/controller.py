from flask import render_template #request
from app import app
from app.models.event_class import *
#from app.models.task import *


@app.route('/')
def index():
    #return "hello world"
    return render_template('index.html', title ='Home ')

# @app.route('/add-task', methods = ['POST'])
# def add_task():
#     task_title = request.form['title']
#     task_desc = request.form['description']
#     new_task = Task(task_title, task_desc, False)
#     add_new_task(new_task)
#     return render_template('index.html', title = 'Home', tasks = tasks)