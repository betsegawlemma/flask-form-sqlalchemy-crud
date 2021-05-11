from flask import Flask
from flask_sqlalchemy import SQLAlchemy

    
app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = '5791628',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///todos.db'
)

db = SQLAlchemy(app)

@app.cli.command('init-db')
def init_db_command():
    db.create_all()

from . import tasks

app.register_blueprint(tasks.bp)