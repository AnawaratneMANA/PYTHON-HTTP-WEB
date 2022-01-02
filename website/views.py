# This file includes standard routes.
from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from datetime import datetime
from . import db


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash("Note is too short!", category='error')
        else:
            date = datetime.now() # Date time default in the schema not working.
            new_note = Note(data=note, user_id=current_user.id, date=date)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template('home.html', user=current_user)

@view.route('/delete-note', methods=['POST'])