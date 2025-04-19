---
title: Commercial Project-Fullstack-模拟考试系统Simulate Exam
date: 2024-03-23 00:00:06 +0800
tags:
  - SpringBoot
  - Vue
  - Backend
  - Frontend
categories:
  - Fullstack
description: 
  A simulate exam system in web and use WeChat to login.
image:
 path: /attachments/商单-全栈-模拟考试系统/image.png
 lqip: data:image/webp;base64,UklGRkYAAABXRUJQVlA4IDoAAABQAwCdASoUAAwAPxFysFAsJqSisAgBgCIJZwAAW+x9f78gAAD+6nyBNWG/WZ5N/hYYNwnRrOS8AAAA
 alt: 商单-全栈-模拟考试系统
pin: true
---

## 商单-全栈-模拟考试系统

浙江建筑模拟考试系统

Responsible for `architecture design`, `back-end development`, and `front-end wechat login guidance`.

## 介绍

网页（PC+手机）+ 后端 + 后台

1. springboot + vue
2. 必须绑定微信登录
3. 后台需开通账户，设置时限等
4. 考试错题，收藏，历史记录
5. 随机考题
6. 题库excel导入导出

## 难点
1. 微信登录
   1. 微信公众号设置
   2. 微信公众号和服务器之间首次沟通的鉴权api
   3. snsapi_base和snsapi_userinfo
2. 随机考题时采用了水库抽样，固定了数量，每个被保留的概率都相同
3. 页面防截图，复制（使用了NoPrint.js）

## 图片

![alt text](/attachments/商单-全栈-模拟考试系统/image.png)

![alt text](/attachments/商单-全栈-模拟考试系统/image-1.png)

![alt text](/attachments/商单-全栈-模拟考试系统/image-2.png)