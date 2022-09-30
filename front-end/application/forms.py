from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField 

from application.models import Task

class TaskForm(FlaskForm):
    task_name = StringField('Task Name')
    task_desc = StringField('Description')
    submit = SubmitField('Submit')