import os

def get_output_filename(base_path='.'):
    folder_name = os.path.basename(os.path.abspath(base_path))
    return f"{folder_name}_백업.md"


EXCLUDE_DIRS = {'node_modules', '.git', 'bin', 'obj', '__pycache__', 'dist', 'build', '.idea', '.vscode', '.venv'}
EXCLUDE_EXTS = {
    '.log', '.lock', '.zip', '.png', '.jpg', '.jpeg', '.gif',
    '.ico', '.exe', '.dll', '.class', '.pyc', '.pyo', '.so',
    '.db', '.sqlite', '.pdf', '.mp4', '.mp3', '.wav'
}

output_file = get_output_filename()

tree_lines = []

def get_language_from_extension(ext):
    ext = ext.lower()
    return {
        '.py': 'python',
        '.js': 'javascript',
        '.ts': 'typescript',
        '.html': 'html',
        '.css': 'css',
        '.json': 'json',
        '.md': 'markdown',
        '.java': 'java',
        '.c': 'c',
        '.cpp': 'cpp',
        '.cs': 'csharp',
        '.xml': 'xml',
        '.sh': 'bash',
        '.yml': 'yaml',
        '.yaml': 'yaml',
        '.go': 'go'
    }.get(ext, '')

def is_excluded(path):
    parts = path.split(os.sep)
    return any(part in EXCLUDE_DIRS for part in parts)

def should_include_file(filename):
    _, ext = os.path.splitext(filename)
    return ext.lower() not in EXCLUDE_EXTS

def build_tree(base_path='.', indent=''):
    items = sorted(os.listdir(base_path))
    for i, name in enumerate(items):
        full_path = os.path.join(base_path, name)
        if is_excluded(full_path):
            continue
        connector = '└── ' if i == len(items) - 1 else '├── '
        if os.path.isdir(full_path):
            tree_lines.append(f"{indent}{connector}📁 {name}")
            build_tree(full_path, indent + ('    ' if i == len(items) - 1 else '│   '))
        else:
            if should_include_file(name):
                tree_lines.append(f"{indent}{connector}📄 {name}")

def dump_structure_and_code(base_path='.'):
    with open(output_file, 'w', encoding='utf-8') as out:
        # 1. 트리 구조 먼저
        tree_lines.clear()
        build_tree(base_path)
        out.write("# 📁 프로젝트 구조\n\n")
        out.write("```\n")
        out.write('\n'.join(tree_lines))
        out.write("\n```\n\n")

        # 2. 각 파일 내용
        for root, dirs, files in os.walk(base_path):
            if is_excluded(root):
                continue
            for filename in files:
                if not should_include_file(filename):
                    continue
                full_path = os.path.join(root, filename)
                if is_excluded(full_path):
                    continue
                rel_path = os.path.relpath(full_path, base_path)
                ext = os.path.splitext(filename)[1]
                lang = get_language_from_extension(ext)

                out.write(f"## 📄 `{rel_path}`\n\n")
                out.write(f"```{lang}\n")
                try:
                    with open(full_path, 'r', encoding='utf-8') as f:
                        out.write(f.read())
                except Exception as e:
                    out.write(f"[Error reading file: {e}]")
                out.write("\n```\n\n")

if __name__ == "__main__":
    dump_structure_and_code()
    print(f"✅ Markdown dump complete: {output_file}")