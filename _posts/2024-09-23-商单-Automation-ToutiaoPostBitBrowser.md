---
title: Commercial Project-Automation-Toutiao Post by Bit Browser
date: 2024-09-23 00:00:05
tags:
  - Python
  - PyQt
  - Automation
categories:
  - Automation
description: 
    Use Selenium to link to Bit Browser debugger address to post Toutiao article as configuration automatically. Use PyQt to build the GUI.
---

# Commercial Project-Automation-Toutiao Post by Bit Browser

## Introduction
Use Selenium to link to Bit Browser debugger address to post Toutiao article as configuration automatically. Use PyQt to build the GUI.

## Libraries used:
* Selenium
* PySide6
* pyside6-uic (to convert .ui file to .py file)
* pyautogui
* pyperclip
* win32gui
* win32process
* win32con

## Difficulties

* Avoid Toutiao's monitoring mechanisms, otherwise your posts will be throttled.
* GUI and business logic should be in different threads.
* Use signal and slot to communicate between threads.

## Screenshots

![alt text](/attachments/商单-Automation-ToutiaoPostBitBrowser/image.png)