import datetime

from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

from . import db
from .models import Task

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.values.get('note')
        score = request.values.get('score')
        new_note = Task(data=note, task_point=score, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()

    return render_template("home.html", user=current_user, name=current_user.first_name)


@views.route('/<int:task_id>', methods=['DELETE'])
@login_required
def delete_note(task_id):
    response = {}
    task = Task.query.get(task_id)
    response['task_id'] = task.id
    if task:
        if task.user_id == current_user.id:
            db.session.delete(task)
            db.session.commit()
            return {
                "success": True,
                "message": "delete success"
            }


@views.route('/<int:task_id>', methods=['POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get(task_id)
    if task:
        if task.user_id == current_user.id:
            updated_note = request.values.get('updated_note')
            updated_score = request.values.get('updated_score')
            task.data = updated_note
            task.task_point = updated_score
            task.date = datetime.datetime.now()
            db.session.commit()
            return {
                "success": True,
                "message": "edit success"
            }