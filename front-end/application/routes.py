from application import app, db
from flask import request, render_template, redirect, url_for
from application.models import *
from application.forms import *

#Read 
@app.route("/", methods=['GET', 'POST'])
def view_all_tasks():
    tasks = Task.query.all()
    return render_template('home.html', tasks=tasks)

#Create 
@app.route('/add_task', methods=['GET','POST'])
def create_new_task():
    form = TaskForm()
    if form.validate_on_submit(): 
        tasks = Task(
            task_name = form.task_name.data,
            task_desc = form.task_desc.data
        )
        db.session.add(tasks)
        db.session.commit()
        return redirect(url_for('view_all_tasks'))
    return render_template('add.html', form=form)



#Update 
@app.route('/complete/<int:task_id>', methods=['GET', 'POST'])
def update(task_id):
    form = TaskForm()
    tasks = Task.query.get(task_id)
    if form.validate_on_submit(): 
        tasks.task_name = form.task_name.data
        tasks.task_desc = form.task_desc.data
        db.session.commit()
        return redirect(url_for('view_all_tasks'))
    elif request.method == 'GET':
        form.task_name.data = tasks.task_name
        form.task_desc.data = tasks.task_desc
    return render_template('update.html', form=form)

#Delete
@app.route('/delete/<int:task_id>')
def delete(task_id):
    tasks = Task.query.get(task_id)
    db.session.delete(tasks)
    db.session.commit()
    return redirect(url_for('view_all_tasks'))