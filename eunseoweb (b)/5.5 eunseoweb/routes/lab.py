from flask import Blueprint, render_template

lab_bp = Blueprint('lab', __name__)

@lab_bp.route("/lab")
def lab():
    return render_template("lab.html")
