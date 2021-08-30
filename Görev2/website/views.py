import json

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user

from . import db
from .models import Task

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        score = request.form.get('score')
        if len(note) < 1:
            flash('Note is too short!', category='error')
        if len(score) < 1:
            flash('Skoru girmeyi unutmayınız', category='error')
        else:
            new_note = Task(data=note, task_point=score, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteid = note['noteid']
    note = Task.query.get(noteid)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
