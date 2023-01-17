import json
from flask import Blueprint, jsonify, render_template, request, flash
from flask_login import login_required, current_user
# from sqlalchemy import DateTime
# from sqlalchemy.sql import func
from . import db
from .models import Note

#urls organization
views =Blueprint('views', __name__)

@views.route('/', methods=['GET','POST']) #decorator
#url to home when this is typed in search bar the following code is run
@login_required
# this means that you must be a login user to acces the home page 

def home():
    if request.method=='POST':
        note= request.form.get('note')
        if len(note)<1:
            flash('Note has not letters dude', category= 'error')
        else:
            #DateTime(timezone=True)date=func.now,
            new_note = Note(data=note, user_id=current_user.id)
            # since you made the note column entries like this
            #  you have to enter all the data in this order with these params:
            #     [SQL: INSERT INTO note (data, date, user_id) VALUES (?, ?, ?)]
            # so this wont work and will cause an error
            #     [parameters: [{'user_id': 2, 'data': 'cooll beans'}]]
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html",user=current_user)

@views.route('/delete-note',methods=['POST'])
def delete_note():
    note =json.loads(request.data)
    noteId = note['noteId']
    note=Note.query.get(noteId)
    if note:
        if note.user_id==current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})