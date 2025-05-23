---
title: FullStack Project - KeyChcker <br /> An app wrapper supplying key access with time and machine limited and communication between wrapper and wrappee.
date: 2023-02-28 00:33:53 +0800
tags:
 - Vue
 - QtC++
 - SpringBoot
 - Java
 - Mysql
 - Python
 - Erupt
 - Backend
 - Frontend
 - FullStack
categories:
 - FullStack
description: 
 Prepare a "coat" for other programs which user can use a time-limited key to log in. User's machine is bound. Supervisor have has his own interface.
 <br />
 Use SHA-256 encrytion, http request, Multi-processes communication(Shared Memory, Message Pipe), Multithread, WinAPI.
 <br />
 QtC++, Springboot, Vue.js, Python, Mysql.
image:
 path: /attachments/全栈项目KeyChcker密钥访问/2023-02-27-21-04-32.png
 lqip: data:image/webp;base64,UklGRkYAAABXRUJQVlA4IDoAAABwAwCdASoUAAwAPxFwsFAsJiSisAgBgCIJZwDKACHe1CMLDAAA/u07nrxGS9vsumR44OvY4IYGwAAA
 alt: KeyChecker
---

## Intro

![alt text](/attachments/全栈项目KeyChcker密钥访问/2023-02-27-20-49-51.png)

[Github link](https://github.com/DuGuYifei/KeyChecker)

Prepare a "coat" for other programs which user can use a time-limited key to log in. Their machines are bound.

The wrapper framework use `mysql` and contains back-end (`Springboot`), back-end supervise interface (`vue`) and user client (`Qt c++`).

Also display a wrappee example by `pyhon` to use the shared memory or message pipe.

[2023补充]

Use Erupt to rebuild the back-end and back-end supervise interface. And I provide it to my first internship company, they pick it as the solution to provide limited AI-WeChat service to customers.

## Tech stack
1. <img alt="alt text" src="https://user-images.githubusercontent.com/25181517/183891303-41f257f8-6b3d-487c-aa56-c497b880d0fb.png"  width="20" height="20"> Springboot - java
2. <img alt="alt text" src="https://user-images.githubusercontent.com/25181517/117448124-a2da9800-af3e-11eb-85d2-bd1b69b65603.png"  width="20" height="20"> Vue.js - javascript, html, css
3. <img alt="alt text" src="/attachments/全栈项目KeyChcker密钥访问/qt.png"  width="20" height="20"> Qt desktop - C++
5. <img alt="alt text" src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png"  width="20" height="20"> Python script
6. <img alt="alt text" src="https://user-images.githubusercontent.com/25181517/183896128-ec99105a-ec1a-4d85-b08b-1aa1620b2046.png"  width="20" height="20"> Database - MySQL


* <img alt="alt text" src="https://user-images.githubusercontent.com/25181517/192107854-765620d7-f909-4953-a6da-36e1ef69eea6.png"  width="20" height="20"> Http request
* <img alt="alt text" src="https://user-images.githubusercontent.com/25181517/186884150-05e9ff6d-340e-4802-9533-2c3f02363ee3.png"  width="20" height="20"> WinAPI - C++, python
* <img alt="alt text" src="/attachments/全栈项目KeyChcker密钥访问/multiprocess.png"  width="20" height="20"> Multi-processes communication - Shared Memory, Message Pipe
* <img alt="alt text" src="/attachments/全栈项目KeyChcker密钥访问/multithread.png"  width="20" height="20"> Multithread in Qt C++
* <img alt="alt text" src="https://user-images.githubusercontent.com/25181517/117207330-263ba280-adf4-11eb-9b97-0ac5b40bc3be.png"  width="20" height="20"> Test by Docker

## TODO
- [x] Give log-in func in back-end supervise interface
- [x] Use JWT token in no.1 of todo list
