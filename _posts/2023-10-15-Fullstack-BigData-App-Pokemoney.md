---
title: 【⭐⭐⭐⭐⭐】FullStack-BigData-App-Pokemoney
date: 2023-10-15 07:36:28 +0800
tags:
 - Java
 - BigData
 - Flutter
 - Apk
 - Sqlite
 - SpringBoot
 - Microservice
 - Redis
 - MySQL
 - ShardingSphere
 - Zookeeper
 - Dubbo
 - Nacos
 - Higress
 - Eureka
 - SpringCloud
 - SpringCloudGateway
 - Kafka
 - Hadoop
 - HBase
 - Hive
 - Spark
 - Nifi
 - Doris
 - Docker
 - Backend
 - Frontend
 - FullStack
categories:
 - FullStack
description: 
   ​Pokemoney is a personal finance app supporting offline and online modes with multi-device synchronization. Built with Flutter and SQLite on the frontend, and a robust backend stack, it enables scalable, distributed data processing.<br>
   The system is built on a modern lakehouse architecture with a microservice-based real-time data pipeline, combining Kafka, Spark, HDFS, Hive, and NiFi for scalable data ingestion, processing, and warehousing. It also integrates a polyglot backend with Redis, MySQL, and HBase, orchestrated via Dubbo, Nacos, and Docker, supporting Dubbo, Triple(gRPC like), RESTful and GraphQL APIs. <br>
   Due to the budge limit, I bought two small servers and my own laptop to deploy the services separately.
image:
 path: /attachments/FullStack-BigData-App-Pokemoney/login_page.png
 lqip: data:image/webp;base64,UklGRlgAAABXRUJQVlA4IEwAAACwAwCdASoUAAwAPxFwsFAsJiSisAgBgCIJZwDG9BwbgjPTJJciAAD+7WF2z8MjknSrkzEEE6bg7/sBQsJe1JBQ7JIeBiRLM1lRp8AA
 alt: Pokemoney
pin: true
---

## 代码链接

[Pokemoney记账软件](https://github.com/DuGuYifei/Pokemoney)

## 项目介绍
Pokemoney = poke + money = pocket + money = 宝可梦 :)

An accounting software that supports both offline and online modes, as well as multi-device login. Each device can switch between accounts, create multiple funding sources, different ledgers, and categorized directories.

The backend supports a large number of users, can be deployed via Docker, connects to a big data platform, and allows the creation of a personal data warehouse.

可离线+联网并且多设备登录的记账软件，一个设备可切换账户，创建多个资金源和不同账本以及不同目录。

后台支持大量用户，同时docker搭建并连接大数据平台，以及创建自己的数据仓库。

## 项目图片

### 技术栈
1. APP：Flutter + sqlite
2. 后端：
   1. (deprecated) SpringCloud + Eureka + SpringCloudGateway
   2. Dynamic Thread Pool (线程池) 
   3. Dubbo
   4. Nacos
   5. Higress
   6. Redis cluster
   7. MySQL cluster + Shardingsphere
      1. Sharding
      2. Read/Write Splitting
   8. Zookeeper (分布式锁)
   9. Leaf (美团分布式ID基于Snowflake)
   10. 大数据平台使用到:
      1.  Kafka
      2.  Hadoop
      3.  HBase
      4.  Hive
      5.  Spark
      6.  Nifi
      7.  Doris
   11. 部署：Docker
   12. 语言：java
   13. Protocal:
       1.  RESTful
       2.  GraphQL
       3.  Triple (Dubbo)
       4.  gRPC

### 难点
1. 有限时间内迅速上手并使用每个技术 / Quickly learn and utilize each technology within a limited timeframe
2. docker部署自己的大数据平台 / Deploy your own big data platform using Docker
3. 项目可离线加联网并且多设备登录的同步方式 / Implement synchronization for offline and online modes with multi-device login support
4. 其他常规：分布式锁，异步，kafka消息队列 / Other common components: distributed locking, asynchronous processing, Kafka message queue

### 手机端 flutter

<div style="text-align:center;">
    <img alt="alt text" src="/attachments/FullStack-BigData-App-Pokemoney/login_page.png" width="30%" style="display:inline-block;">
    <img alt="alt text" src="/attachments/FullStack-BigData-App-Pokemoney/Ledger_books.png" width="30%" style="display:inline-block;">
    <img alt="alt text" src="/attachments/FullStack-BigData-App-Pokemoney/The_app_navigation.png" width="30%" style="display:inline-block;">
    <img alt="alt text" src="/attachments/FullStack-BigData-App-Pokemoney/main_page_1.png" width="30%" style="display:inline-block;">
    <img alt="alt text" src="/attachments/FullStack-BigData-App-Pokemoney/Funds_main.png" width="30%" style="display:inline-block;">
    <img alt="alt text" src="/attachments/FullStack-BigData-App-Pokemoney/Funds_MoreDetails.png" width="30%" style="display:inline-block;">
</div>

### 后端架构
1. v1: SpringClould + Eureka + SpringCloudGateway
![alt text](/attachments/FullStack-BigData-App-Pokemoney/Frame_1.png)
2. v2: Dubbo + Nacos + SpringCloudGateway
![alt text](/attachments/FullStack-BigData-App-Pokemoney/Frame_2.png) 
3. v3: Dubbo + Nacos + Higress
![alt text](/attachments/FullStack-BigData-App-Pokemoney/Frame_6.png)

### 大数据架构
1. v1
   ![alt text](/attachments/FullStack-BigData-App-Pokemoney/Frame_3.png)
2. v2
   ![alt text](/attachments/FullStack-BigData-App-Pokemoney/Frame_4.png) 