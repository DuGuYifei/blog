---
title: Commercial Project-Fullstack-Market Snapshot行情监控截图
date: 2024-09-23 00:00:05
tags:
  - Python
  - QtC++
  - Go
categories:
  - Fullstack
description: 
  This project involves developing a server-side application using Go language, which performs real-time and scheduled daily screenshots of specific sections of a financial market software. These screenshots are timestamped and later concatenated into a single image. Special handling is applied to weekends and holidays, including scenarios where they overlap. On the client side, the application utilizes Qt C++ and requires a password for users to access and receive the images.
---

# Commercial Project-Fullstack-Market Snapshot行情监控截图

* This project involves developing a server-side application using Go language, which performs real-time and scheduled daily screenshots of specific sections of a financial market software. 
* These screenshots are timestamped and later concatenated into a single image. 
* Additionally, screenshots taken on the eve of holidays are placed in the second column, and remove it after the holiday.
* The real-time screenshots will always be in first column, while the scheduled screenshots will be placed as the time sequence.
* The system will pause screenshot operations during weekends and holidays, resuming on the following working day with the appropriate datetime stamped. 
* The project also handles scenarios where weekends and holidays overlap. 
* On the client side, the application utilizes Qt C++ and requires a password for users to access and receive the images.

![alt text](/attachments/商单-Fullstack-MarketSnapshot行情监控截图/3af2ab5a961874365fe7a065c1b607d.png)