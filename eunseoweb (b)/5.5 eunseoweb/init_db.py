import sqlite3

# DB 연결 (없으면 생성됨)
conn = sqlite3.connect("data/log.db")
cursor = conn.cursor()

# logs 테이블 생성
cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("✅ logs 테이블 생성 완료")