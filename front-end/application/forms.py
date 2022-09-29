from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField 

class TaskForm(FlaskForm):
    task_name = StringField('Task Name')
    task_desc = StringField('Description')