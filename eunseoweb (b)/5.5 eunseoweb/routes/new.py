from flask import Blueprint, render_template

new_bp = Blueprint('new', __name__)

@new_bp.route("/new")
def new():
    return render_template("new.html")