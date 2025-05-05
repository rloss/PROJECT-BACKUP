import os
import json

# 생성할 디렉토리 목록
directories = [
    "routes",
    "data",
    "static"
]

# 생성할 파일들: 경로와 초기 내용
files = {
    "routes/__init__.py": "",
    "routes/home.py": "",
    "routes/log.py": "",
    "routes/lab.py": "",
    "data/log.json": json.dumps([], indent=2, ensure_ascii=False),
    "static/style.css": "",
    "static/sections.css": ""
}

# 디렉토리 생성
for d in directories:
    os.makedirs(d, exist_ok=True)

# 파일 생성
for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ 구조 생성 완료!")