---
title: Blog-jekyll_GithubPage
date: 2025-04-11 20:00:00 +0800
tags:
- Blog
categories:
- Blog
description: 使用Github Pages + jekyll + Chirpy 搭建个人博客
image:
 path: /attachments/2025-04-11-Blog-jekyll_GithubPage/image.png
 alt: Blog-jekyll_GithubPage  
---

# 安装环境

```bash
# 安装ruby
sudo dnf update -y
sudo dnf groupinstall "Development Tools" -y
sudo dnf install ruby ruby-devel zlib-devel @development-tools redhat-rpm-config -y

# 安装nvm，用来安装node，启用yarn
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
# 重启终端，使nvm生效
# 安装node
nvm ls-remote
# 查看可用版本，比如我安装LTS
nvm install 22.14.0
# 启用yarn
corepack enable

# 安装jekyll和bundler
sudo gem install bundler jekyll
# 检查环境
ruby -v
jekyll -v
node -v
yarn -v
```

# 获取 Chirpy 模板

```bash
git clone git@github.com:cotes2020/chirpy-starter.git my-blog
cd my-blog
```

# 安装依赖

```bash
bundle install
yarn
```

# 启动本地服务

```bash
bundle exec jekyll s
```

访问`http://localhost:4000`

# 修改博客信息

编辑 `_config.yml`，设置博客标题、作者、链接等

# 部署到Github Pages

方式一（推荐）：GitHub Actions 自动部署

Chirpy 已内置 `.github/workflows/pages-deploy.yml`，你只需：

1. 仓库设置为 Public
2. GitHub 仓库 → Settings → Pages → 选择 GitHub Actions
3. 每次 push 到 main 分支就会自动部署，访问对应的github.io地址即可

方式二：手动部署
```
JEKYLL_ENV=production bundle exec jekyll build
```

然后把 _site/ 里的内容推送到 gh-pages 分支：
```bash
git checkout --orphan gh-pages
git rm -rf .
cp -r _site/* .
git add .
git commit -m "Deploy"
git push origin gh-pages
```

## favicon

放到`assets/img/favicon/`目录下，命名为`favicon.ico`