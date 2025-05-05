import os

BASE_DIR = "insight_flow"

folders = [
    f"{BASE_DIR}/data",
    f"{BASE_DIR}/routes",
    f"{BASE_DIR}/templates",
    f"{BASE_DIR}/static/images"
]

files = {
    f"{BASE_DIR}/app.py": "# app.py - Flask 앱 실행 진입점\n",
    f"{BASE_DIR}/init_db.py": "# init_db.py - DB 초기화 스크립트\n",
    f"{BASE_DIR}/requirements.txt": "flask\n",
    f"{BASE_DIR}/README.md": "# Insight Flow - 자기계발 인사이트 블로그\n",
    f"{BASE_DIR}/routes/__init__.py": "",
    f"{BASE_DIR}/routes/home.py": "# home.py - 메인 페이지 라우트\n",
    f"{BASE_DIR}/routes/post.py": "# post.py - 글 쓰기, 보기, 수정, 삭제\n",
    f"{BASE_DIR}/routes/filter.py": "# filter.py - 카테고리/태그 필터 라우트\n",
    f"{BASE_DIR}/routes/community.py": "# community.py - 커뮤니티 (미구현)\n",
    f"{BASE_DIR}/templates/base.html": "<!-- base.html - 전체 레이아웃 템플릿 -->\n",
    f"{BASE_DIR}/templates/home.html": "<!-- home.html - 메인 페이지 -->\n",
    f"{BASE_DIR}/templates/post_list.html": "<!-- post_list.html - 글 목록 -->\n",
    f"{BASE_DIR}/templates/post_detail.html": "<!-- post_detail.html - 글 상세 -->\n",
    f"{BASE_DIR}/templates/post_form.html": "<!-- post_form.html - 글쓰기/수정 폼 -->\n",
    f"{BASE_DIR}/templates/category_list.html": "<!-- category_list.html -->\n",
    f"{BASE_DIR}/templates/tag_list.html": "<!-- tag_list.html -->\n",
    f"{BASE_DIR}/templates/community.html": "<!-- community.html -->\n",
    f"{BASE_DIR}/static/style.css": "/* style.css - 기본 스타일 */\n",
    f"{BASE_DIR}/static/script.js": "// script.js - 사이드바 토글 등 JS\n"
}

def create_project():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"📁 폴더 생성됨: {folder}")

    for path, content in files.items():
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"📄 파일 생성됨: {path}")

    print("\n✅ Insight Flow 프로젝트 기본 구조 생성 완료!")

if __name__ == "__main__":
    create_project()
