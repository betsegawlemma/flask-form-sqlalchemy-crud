from todos import db 

class TaskModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), nullable = False)
    description = db.Column(db.String(1000), nullable = True)
    due_date = db.Column(db.String(20), nullable = True)
