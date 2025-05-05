# community.py - 커뮤니티 (미구현)
from flask import Blueprint

community_bp = Blueprint("community", __name__, url_prefix="/community")

@community_bp.route("/")
def community_home():
    return "커뮤니티 기능 예정"
