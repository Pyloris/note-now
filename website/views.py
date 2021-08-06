from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=["GET", "POST"])
@login_required
def home():
	if request.method == "POST":
		note = request.form.get("note")
		if len(note) < 1:
			flash("Note is Empty!", category="error")
		else:
			new_note = Note(data=note, user_id=current_user.id)
			db.session.add(new_note)
			db.session.commit()
			flash("Note added!", category="success")

	return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=["POST"])
def delete_note():
	noteId = request.form.get('noteId')
	note = Note.query.get(noteId)
	if note:
		if note.user_id == current_user.id:
			db.session.delete(note)
			db.session.commit()
	return redirect(url_for("views.home"))