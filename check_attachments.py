#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import re
import shutil

POSTS_DIR = Path("./_posts")
ATTACH_DIR = Path("./attachments")

ATTACH_RE = re.compile(r"/attachments/([^/\s]+)/")

def main():
    for md in POSTS_DIR.glob("*.md"):
        name = md.stem
        text = md.read_text(encoding="utf-8")

        folders = set(ATTACH_RE.findall(text))

        for folder in folders:
            if folder == name:
                continue

            old_dir = ATTACH_DIR / folder
            new_dir = ATTACH_DIR / name

            print(f"\n[MD] {md}")
            print(f" folder: {folder} -> {name}")

            # 修改markdown
            new_text = text.replace(
                f"/attachments/{folder}/",
                f"/attachments/{name}/"
            )

            if new_text != text:
                md.write_text(new_text, encoding="utf-8")
                print(" markdown updated")

            # 重命名目录
            if old_dir.exists():
                if not new_dir.exists():
                    shutil.move(old_dir, new_dir)
                    print(f" rename: {old_dir} -> {new_dir}")
                else:
                    print(f" skip rename (target exists): {new_dir}")
            else:
                print(f" skip rename (not found): {old_dir}")

            text = new_text


if __name__ == "__main__":
    main()