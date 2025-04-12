---
title: Drone Simulation + GIS Monitor = UE + MS Airsim + Cesium + Nodejs + Google 3d tile map
date: 2023-06-07 00:00:00 +0800
tags:
 - UE
 - Game
 - GIS
categories:
 - Game
description:
    A drone simulation and GIS monitor system based on UE + MS Airsim + Cesium + Nodejs + Google 3d tile map.
    <br />
    The drone simulation system is based on UE + MS Airsim + Cesium for Unreal + Google 3d tile map, and the GIS monitor system is based on Cesium + Nodejs + simple streaming camera from simulated drone by UDP.
    <br />
    The drone simulation system can be used to simulate the flight of drones, and the GIS monitor system can be used to monitor the flight of drones in real time.
image:
 path: /attachments/2023-06-07-DroneSimulation_GISMonitor/image.png
 lqip: data:image/webp;base64,UklGRoIAAABXRUJQVlA4IHYAAADQAwCdASoUAAwAPxFwsFAsJiSisAgBgCIJYgAAW9tk+4dKw2bGNvAA/I+WItr4rxThHc+1W84UHnhegXaTkMpO0rLNlG4tIl6usAfd466fp02b58vE7iyyQJk/rJhhvi5BHv2vJQxTAeiDg0nC7/hSEHwEfBAA
 alt: Drone Simulation and GIS Monitor
pin: true
---

## 项目介绍

* 代码：[https://github.com/DuGuYifei/DroneSimulatorMonitor](https://github.com/DuGuYifei/DroneSimulatorMonitor)
* 视频：[https://www.bilibili.com/video/BV1wz4y1i7sW/](https://www.bilibili.com/video/BV1wz4y1i7sW/)

{% include embed/bilibili.html id='BV1wz4y1i7sW' %}

This project presents a high-fidelity real-time drone simulation and geospatial visualization platform by tightly integrating Microsoft AirSim, Unreal Engine, Cesium for Unreal, and Node.js.

## Core Architecture and Capabilities:

* Physically UAV Simulation
    
    Leveraging Microsoft AirSim within Unreal Engine, the system simulates drone dynamics and flight behavior in a photorealistic environment. Real-world terrain and building data are streamed using Cesium for Unreal, with Google 3D Tiles integrated via API key to provide high-resolution, geo-accurate maps.

* Multi-Camera Streaming via UDP
    
    Virtual cameras are mounted on the simulated drone, and their live video feeds are captured and transmitted via UDP to a Node.js backend server. This setup mimics onboard video transmission in real UAV systems.

* Web-Based Geospatial Visualization
    
    The backend processes incoming data and renders it on a web interface using CesiumJS. Real-time GPS telemetry is used to visualize the drone's current position on a global map. Additionally, the system renders a dynamic camera frustum to depict the field of view of any selected onboard camera, enabling spatial awareness of what the drone is observing.

* Live Multi-Camera Monitoring
    The web client supports real-time display of image feeds from all drone-mounted cameras, allowing for simultaneous multi-perspective monitoring directly from the browser.

This platform enables a robust foundation for applications in autonomous navigation, remote sensing, surveillance system prototyping, and digital twin environments, offering an end-to-end simulation-to-visualization pipeline in a geographically accurate 3D context.