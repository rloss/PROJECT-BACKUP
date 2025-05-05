# routes/post.py

from flask import Blueprint, render_template, request, redirect
from datetime import datetime
from models import db, Post

post_bp = Blueprint("post", __name__, url_prefix="/post")


@post_bp.route("/write", methods=["GET", "POST"])
def write_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        author = request.form["author"]
        categories = ",".join(request.form.getlist("categories"))
        tags = request.form["tags"]
        created_at = datetime.now().isoformat()

        new_post = Post(
            title=title,
            content=content,
            author=author,
            categories=categories,
            tags=tags,
            created_at=created_at
        )
        db.session.add(new_post)
        db.session.commit()

        return redirect("/post")

    category_options = ["기술", "경제", "트렌드", "사회", "기타"]
    return render_template("post_form.html", categories=category_options)


@post_bp.route("/")
def post_list():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template("post_list.html", posts=posts)


@post_bp.route("/<int:post_id>")
def post_detail(post_id):
    post = Post.query.get(post_id)
    if not post:
        return "해당 글을 찾을 수 없습니다.", 404
    return render_template("post_detail.html", post=post)


@post_bp.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        return "글이 존재하지 않습니다.", 404

    if request.method == "POST":
        post.title = request.form["title"]
        post.content = request.form["content"]
        post.author = request.form["author"]
        post.categories = ",".join(request.form.getlist("categories"))
        post.tags = request.form["tags"]
        db.session.commit()
        return redirect(f"/post/{post_id}")

    post_data = {
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "author": post.author,
        "categories": post.categories.split(",") if post.categories else [],
        "tags": post.tags
    }
    category_options = ["기술", "경제", "트렌드", "사회", "기타"]

    return render_template("post_form.html", post=post_data, categories=category_options, mode="edit")


@post_bp.route("/delete/<int:post_id>", methods=["POST"])
def delete_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        return "해당 글이 존재하지 않습니다.", 404
    db.session.delete(post)
    db.session.commit()
    return redirect("/post")

