from application import app
from flask import request, render_template, redirect, url_for
from application.models import *
from application.forms import *

#Create 
@app.route('/add_task', methods=['GET','POST'])
def create_new_task():
    form = TaskForm()
    if form.validate_on_submit(): 
        tasks = Task(
            taskname = form.task_name.data,
            taskdesc = form.task_desc.data
        )
        db.session.add(tasks)
        db.session.commit()
        return redirect(url_for('view_all_tasks'))
    return render_template('add.html', form=form)

#Read 
@app.route('/')
def view_all_tasks():
    tasks = Task.query.all()
    return render_template('home.html', tasks=tasks)

#Update 

#Delete
@app.route('/delete/<int:task_id>')
def delete(task_id):
    tasks = Task.query.get(task_id)
    db.session.delete(tasks)
    return redirect(url_for('index'))