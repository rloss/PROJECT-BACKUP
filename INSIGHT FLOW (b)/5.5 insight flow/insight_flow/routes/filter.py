from flask import Blueprint, render_template
from models import Post

filter_bp = Blueprint("filter", __name__, url_prefix="/filter")

@filter_bp.route("/category/<name>")
def category(name):
    posts = Post.query.filter(Post.categories.like(f"%{name}%"))\
                      .order_by(Post.created_at.desc()).all()
    return render_template("post_list.html", posts=posts, current_category=name)
