---
title: Commercial Project-FullStack-在线图书馆课元Library
date: 2024-03-23 00:00:05 +0800
tags:
  - SpringBoot
  - Solr
  - Vue
  - Backend
  - Frontend
  - FullStack
categories:
  - FullStack
description:
  一个在线图书馆，包括前端展示，后台管理，后端开发，以及solr搜索引擎的使用。但是受到了最终商家服务器的性能和带宽限制，因此需要对前端和后端进行优化。
image:
 path: /attachments/商单-全栈-在线图书馆课元Library/image.png
 lqip: data:image/webp;base64,UklGRnYAAABXRUJQVlA4IGoAAADQAwCdASoUAAwAPxFysFAsJqSisAgBgCIJYwDG9CG+2G9NJ/uE14AA/up7yTYg+v0fkZ50iFakbXBFErxoPYuv4V7er9PkPanPJxDKsi+Rr8QfWbkL/f0fxL8BqBdn5TeIfiMKw6kyQAAA
 alt: 商单-全栈-在线图书馆课元Library
pin: true
---

## 商单-全栈-在线图书馆课元Library

网页：[Keyuan Library](https://kybook.witnew.net/)

Responsible for `architecture design` and `backend development`.

## 介绍

1. 存在 管理员 + 组织管理员 + 读者
2. session管理
3. springboot + mysql + solr
4. 其中solr是搜索引擎来对图书进行检索
5. 前端（PC + 移动） + 后台 + 后端
6. 将美国图书分类映射到中图分类法
7. 阅读和下载数量限制
8. 在线阅读pdf + epub

## 难点
1. solr，实际在java中使用感觉和常规的数据库操作差不太多，注意一些特殊语法就行。
2. 组织多级管理，鉴权，前端镜像
3. 映射时候使用了python机器学习进行相似度匹配，并生成json
4. 在线阅读 pdf + epub，从前端解决了
5. 最终商家部署的提供的服务器是通过反向代理来实现的，因此要注意传递的效率，减少传值的次数和数量
6. 每周，每月，热点，新书受限于服务器的性能，必须优化
7. 商家会除了自身的部署，还会给客户提供镜像，但是总部还需要对镜像的用户进行管理，因此后台需要分多级管理，不同的层级有不同的权限，并且对ip还需要进行限制

### 有趣的东西
将封面的2d图片通过css变为3d的图书。[]

## 课元图书馆客户之一：

![alt text](/attachments/商单-全栈-在线图书馆课元Library/image-3.png)

## 设计师初稿
![alt text](/attachments/商单-全栈-在线图书馆课元Library/image.png)

![alt text](/attachments/商单-全栈-在线图书馆课元Library/image-2.png)

![alt text](/attachments/商单-全栈-在线图书馆课元Library/image-1.png)