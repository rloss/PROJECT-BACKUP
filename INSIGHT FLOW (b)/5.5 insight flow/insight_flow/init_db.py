# init_db.py - DB 초기화 스크립트
import sqlite3
import os
from datetime import datetime

# DB 파일 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "data", "posts.db")

# DB 연결 및 테이블 생성
def init_db():
    os.makedirs(os.path.join(BASE_DIR, "data"), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # posts 테이블 생성
    c.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author TEXT NOT NULL,
            categories TEXT NOT NULL,
            tags TEXT,
            created_at TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
    print("✅ posts.db 초기화 완료!")

if __name__ == "__main__":
    init_db()
