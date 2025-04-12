---
title: Notes-docsify
date: 2025-04-12 20:00:00 +0800
tags:
- Blog
categories:
- Blog
description: 使用Github Pages + docsify 搭建笔记博客
image:
 path: /attachments/2025-04-12-Notes-docsify/image.png
 lqip: data:image/webp;base64,UklGRlIAAABXRUJQVlA4IEYAAACQAwCdASoUAAwAPxFysVAsJqSisAgBgCIJaQAAW+umowQF8j4AAP7tQAWP9Y8SkC8NDv3Qh+eVWwrDNeC5HkEV5QcoAAAA
 alt: Notes-docsify
---

## 使用方式

[docsify 文档](https://docsify.js.org/)

```bash
npm i docsify-cli -g
docsify init ./docs
docsify serve docs
```

## Main problem to solve

### download not markdown file or preview pdf by the feature of browser

total code see last of page

```js
plugins: [
        function reload_page(hook, vm) {
          // hook.init(function () {
          //   console.log("init");
          // });
          // hook.mounted(function () {
          //   console.log("mounted");
          // });
          // hook.beforeEach(function (markdown) {
          //   console.log("beforeEach");
          //   return markdown;
          // });
          // hook.afterEach(function (html) {
          //   console.log("afterEach");
          //   return html;
          // });
          // hook.doneEach(function () {
          //   console.log("doneEach");
          // });
          // hook.ready(function () {
          //   console.log("ready");
          // });

          hook.beforeEach(function (markdown) {
            const path = location.pathname;
            if (/\.[a-z0-9]+(\?.*)?$/i.test(path)) {
              console.log("刷新界面");
              location.reload();
              return;
            }
          });
        },
      ],
```

### sidebar - catalog

```python
import os
from pathlib import Path

def generate_sidebar(path, visible_root):
    ignore_files = {
        "gitp.cmd", "gitp.sh", "gitpf.cmd", "_sidebar.md", "README.md",
        ".gitignore", ".nojekyll", "catalog.py", "index.html", "CNAME", "_404.md"
    }
    ignore_dirs = {".obsidian", ".git", "_attachments", "MyGameDesign", "images", "vue学习用案例模板"}

    entries = []
    for entry in sorted(os.listdir(path), key=lambda s: (0 if s.startswith('_') else 1, s)):
        full_path = Path(path) / entry
        if entry in ignore_files or any(part in ignore_dirs for part in full_path.parts):
            continue

        if full_path.is_dir():
            # 递归子目录时，visible_root 变为子目录的路径
            # join visible_root and entry
            temp_visible_root = visible_root / entry
            subdir_entries = generate_sidebar(full_path, temp_visible_root)
            if subdir_entries:
                entries.append(f"- {entry}")
                entries.extend([f"    {line.replace('](', f']({entry}/')}" for line in subdir_entries])

        # elif full_path.suffix == ".md":
        else:
            # 相对于 visible_root 计算路径
            rel_path = full_path.relative_to(visible_root).as_posix()
            print(rel_path)
            entries.append(f"- [{entry[:-3]}]({rel_path})")

    if entries:
        sidebar_path = Path(path) / "_sidebar.md"
        with open(sidebar_path, "w", encoding="utf-8") as f:
            # 添加返回上级目录, 即 visible_root
            if visible_root != base_path:
                f.write(f"- [返回上级目录](../_sidebar.md)\n")
            f.write("\n".join(entries))

    return entries

# 起始路径
base_path = Path(".")
# 调用时，把当前目录作为 base_path，同时 visible_root 也设置为 base_path
generate_sidebar(base_path, base_path)
```

## total code

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>Document</title>
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
  <meta name="description" content="Description">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify@4/lib/themes/vue.css">
  <!-- <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify-sidebar-collapse/dist/sidebar-folder.min.css" /> -->
  <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify-sidebar-collapse/dist/sidebar.min.css" />
</head>

<body>
  <div id="app"></div>
  <script>
    window.$docsify = {
      routerMode: 'history',
      name: "Notes",
      relativePath: true,
      // 侧边栏文档目录
      loadSidebar: true,
      subMaxLevel: 99,
      sidebarDisplayLevel: 1, // set sidebar display level
      // 跳转后自动到顶部
      auto2top: true,
      // coverpage: true,
      // PLUGINS
      // ----------------------------------------------------------------
      // 页面右侧toc
      toc: {
        tocMaxLevel: 2,
        target: "h2, h3, h4, h5, h6",
      },
      // 全文搜索
      search: {
        depth: 6,
        noData: "没有搜到!",
        placeholder: "搜索...",
        // 避免搜索索引冲突,同一域下的多个网站之间
        // namespace: "website-1",
      },
      // 底部导航
      pagination: {
        previousText: "上一页",
        nextText: "下一页",
        crossChapter: true,
        crossChapterText: true,
      },
      plugins: [
        function reload_page(hook, vm) {
          // hook.init(function () {
          //   console.log("init");
          // });
          // hook.mounted(function () {
          //   console.log("mounted");
          // });
          // hook.beforeEach(function (markdown) {
          //   console.log("beforeEach");
          //   return markdown;
          // });
          // hook.afterEach(function (html) {
          //   console.log("afterEach");
          //   return html;
          // });
          // hook.doneEach(function () {
          //   console.log("doneEach");
          // });
          // hook.ready(function () {
          //   console.log("ready");
          // });

          hook.beforeEach(function (markdown) {
            const path = location.pathname;
            if (/\.[a-z0-9]+(\?.*)?$/i.test(path)) {
              console.log("刷新界面");
              location.reload();
              return;
            }
          });
        },
      ],
    };
  </script>
  <!-- Docsify v4 -->
  <script src="//cdn.jsdelivr.net/npm/docsify@4"></script>
  <script src="//cdn.jsdelivr.net/npm/docsify@4/lib/plugins/external-script.min.js"></script>

  <!-- 代码高亮  //unpkg.com/prismjs/components/ -->
  <script src="//unpkg.com/prismjs/components/prism-bash.js"></script>
  <script src="//unpkg.com/prismjs/components/prism-python.js"></script>
  <script src="//unpkg.com/prismjs/components/prism-cmake.js"></script>
  <script src="//unpkg.com/prismjs/components/prism-java.js"></script>
  <script src="//unpkg.com/prismjs/components/prism-csharp.js"></script>
  <script src="//unpkg.com/prismjs/components/prism-docker.js"></script>
  <script src="//unpkg.com/prismjs/components/prism-powershell.js"></script>
  <script src="//unpkg.com/prismjs/components/prism-go.js"></script>

  <!-- 侧边栏目录折叠 -->
  <script src="//cdn.jsdelivr.net/npm/docsify-sidebar-collapse/dist/docsify-sidebar-collapse.min.js"></script>

  <!-- 多tab支持 -->
  <!-- <script src="https://cdn.jsdelivr.net/npm/docsify-tabs@latest"></script> -->

  <!-- 代码复制 -->
  <script src="//cdn.jsdelivr.net/npm/docsify-copy-code/dist/docsify-copy-code.min.js"></script>

  <!-- 底部 上一页下一页 -->
  <script src="//cdn.jsdelivr.net/npm/docsify-pagination/dist/docsify-pagination.min.js"></script>

  <!-- 全文搜索 -->
  <script src="//cdn.jsdelivr.net/npm/docsify@4/lib/plugins/search.js"></script>

  <!-- 图片放大缩小 -->
  <script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/zoom-image.min.js"></script>

  <!-- 页面右侧 TOC -->
  <script src="//cdn.jsdelivr.net/npm/docsify-plugin-toc@1.1.0/dist/docsify-plugin-toc.min.js"></script>

  <!-- emoji -->
  <script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/emoji.min.js"></script>

  <!-- 数学 -->
  <script src="//cdn.jsdelivr.net/npm/katex@latest/dist/katex.min.js"></script>
  <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/katex@latest/dist/katex.min.css" />
  <script src="//cdn.jsdelivr.net/npm/marked@4"></script>

  <!-- CDN files for docsify-katex -->
  <script src="//cdn.jsdelivr.net/npm/docsify-katex@latest/dist/docsify-katex.js"></script>
  <!-- or <script src="//cdn.jsdelivr.net/gh/upupming/docsify-katex@latest/dist/docsify-katex.js"></script> -->

</body>

</html>
```

