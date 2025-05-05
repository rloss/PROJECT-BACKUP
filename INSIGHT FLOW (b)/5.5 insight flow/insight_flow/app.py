# app.py - Flask 앱 실행 진입점
from flask import Flask
from config import Config
from models import db
from routes.home import home_bp
from routes.post import post_bp
from routes.filter import filter_bp
from routes.community import community_bp  # 아직 미구현이지만 구조만 포함

import os

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = os.environ.get("SECRET_KEY", "super-default-dev-key")  # CSRF/세션 보호용 키

db.init_app(app)
with app.app_context():
    db.create_all()  # DB 초기화

# 라우트 등록
app.register_blueprint(home_bp)
app.register_blueprint(post_bp)
app.register_blueprint(filter_bp)
app.register_blueprint(community_bp)

# 정적 파일 설정 (static/, templates/)
app.static_folder = "static"
app.template_folder = "templates"

port = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)