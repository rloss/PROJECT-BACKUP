# home.py - 메인 페이지 라우트

from flask import Blueprint, render_template
from models import Post  # ✅ 게시글 모델 가져오기

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():
    recent_posts = Post.query.order_by(Post.created_at.desc()).limit(4).all()
    return render_template("home.html", posts=recent_posts)

@home_bp.route("/community")
def community():
    return render_template("community.html")
