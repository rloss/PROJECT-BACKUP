from flask import Flask
from routes.home import home_bp
from routes.log import log_bp
from routes.lab import lab_bp
from routes.new import new_bp
import os

app = Flask(__name__)
app.secret_key = 'eunseo-secret'

# Blueprint 등록
app.register_blueprint(home_bp)
app.register_blueprint(log_bp)
app.register_blueprint(lab_bp)
app.register_blueprint(new_bp)

# Render 등 배포 환경 대비: 환경변수에서 포트 가져오기
port = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)
