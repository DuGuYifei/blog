---
title: Internship-Go-AI WeChat Service
date: 2023-09-23 00:00:00
tags:
  - Go
  - C++
  - Reverse Engineering
categories:
  - Desktop
description: 
    (Legal statement：it is a project branch under the support of Shanghai government which is try to use AI in business field.) Use Reverse Engineering Injection to connect the WeChat service and LLM. Go is use to build the tcp server. One of the dll from public need to be rewritten to satisfy the requirement of the project. Also use Go to create a UI console.
---

# Internship-Go-AI WeChat Service

## Introduction

Use Reverse Engineering Injection to connect the WeChat service and LLM. Go is use to build the tcp server. One of the dll from public need to be rewritten to satisfy the requirement of the project. Also use Go to create a UI console. The dll which is rerwitten is written in C++.

I responsible for the whole project.

* It is still used in the company. 
* It also had other two different versions which is provided to a clothing company and a lawyer company.
* It play the role as customer service and promoter. 
* It reply and send different message in the group chat or personal chat.
* Message by the previous messages and the user's information or comments which written by the colleagues or the user's tags.
* Use heartbeat machanism to notify the administator when the program is down.
* Define some command that can control the service to do some operation by some specific user.

## Difficulties

* Users' sentense is not always send in one time. It may be sent in several times. So the program need to decide when to reply.
* The WeChat account of company may have 9999+ friends. So the program need to consider:
  * The memory using for caching
  * The speed to reply users' message
  * WeChat may consider you are in danger situation and ask you to verify your account if reply different people at the same time.
* When to reply user in group chat, if they not @ account but directly call the account name.