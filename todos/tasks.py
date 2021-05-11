from flask import Blueprint, redirect, render_template, url_for, request
from todos.task_form import TaskForm
from todos.task_model import TaskModel
from . import db

bp = Blueprint('tasks', __name__, url_prefix='/tasks')

@bp.route('/create', methods=['GET', 'POST'])
def create():
    form = TaskForm()
    if form.validate_on_submit():
        task = TaskModel(title = form.title.data, description = form.description.data, due_date = form.due_date.data )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('tasks.list'))
    return render_template('tasks/upsert.html', form  = form)

@bp.route('/list', methods = ['GET'])
def list():
    tasks = TaskModel.query.all()
    return render_template('tasks/list.html', tasks = tasks)

@bp.route('/detail/<int:id>')
def detail(id):
    task = TaskModel.query.get_or_404(id)
    return render_template('tasks/detail.html', task = task)

@bp.route('/edit/<int:id>', methods = ['GET', 'POST'])
def edit(id):
    task = TaskModel.query.get_or_404(id)
    form = TaskForm()
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.due_date = form.due_date.data
        db.session.commit()
        return redirect(url_for('tasks.list'))

    if request.method == 'GET':
        form.title.data = task.title
        form.description.data = task.description
        form.due_date.data = task.due_date
        return render_template('tasks/upsert.html', form = form)

@bp.route('/delete/<int:id>')
def delete(id):
    task = TaskModel.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('tasks.list'))
    