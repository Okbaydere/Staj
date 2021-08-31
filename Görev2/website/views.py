from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user

from . import db
from .models import Task

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.get_json()
        score = request.get_json()
        if note.length < 1 or len(score) < 1:
            flash('Not veya score boş bırakılamaz', category='error')
        else:
            new_note = Task(data=note, task_point=score, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()

    return render_template("home.html", user=current_user, name=current_user.first_name)


@views.route('/<int:task_id>', methods=['POST'])
@login_required
def delete_note(task_id):
    response = {}
    task = Task.query.get(task_id)
    response['task_id'] = task.id
    if task:
        if task.user_id == current_user.id:
            db.session.delete(task)
            db.session.commit()
            return 201
