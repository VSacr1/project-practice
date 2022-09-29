from application import db 

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(30))
    task_desc = db.Column(db.String(100)) 
    