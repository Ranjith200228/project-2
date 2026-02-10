# ⭐ Cloud Conversational AI Platform
### Production-Grade Speech Intelligence System (GCP • Cloud Run • AI APIs)

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-Production-black)
![Google Cloud](https://img.shields.io/badge/Google%20Cloud-Run-success)
![Docker](https://img.shields.io/badge/Containerized-Yes-blueviolet)

---

## 🚀 Live Production Demo

👉 **Launch the Application:**  
https://project2-610853696776.us-east1.run.app/

👉 **Cloud Run Dashboard:**  
https://console.cloud.google.com/run/detail/us-east1/project2/metrics?project=convai-449103

*(Fully deployed serverless AI system — no local setup required.)*

---

## 🧠 Executive Summary

This repository contains a **production-style Conversational AI platform** engineered to process human speech, understand emotional tone, and generate natural voice responses — all delivered through a scalable serverless infrastructure.

The system integrates multiple Google Cloud AI services into a cohesive microservice architecture capable of supporting real-world conversational workloads.

> **Primary Goal:** Demonstrate the design, development, and deployment of an end-to-end cloud-native AI application.

---

## 🔥 Why This Project Stands Out

Most academic projects stop at model building.

This project goes further — showcasing production engineering capabilities:

✅ Cloud-native deployment  
✅ Containerized infrastructure  
✅ AI service orchestration  
✅ Stateless backend design  
✅ Artifact lifecycle management  
✅ Scalable architecture  

---

## ⚡ Core Capabilities

### 🎙️ Intelligent Speech Recognition
- Browser-based audio capture  
- Secure upload pipeline  
- Long-running recognition for higher transcription accuracy  
- Downloadable transcript artifacts  

---

## 🏗️ System Architecture

```mermaid
flowchart LR
  A[Client Browser] --> B[MediaRecorder API - Audio Capture]
  B --> C[Frontend - HTML + JavaScript]
  C --> D[Flask REST API - Docker Container]

  D --> E[Google Speech-to-Text]
  E --> F[Transcript]

  D --> G[Google Natural Language API]
  G --> H[Sentiment Score]

  D --> I[Google Text-to-Speech]
  I --> J[Synthesized Audio]

  F --> K[Artifact Storage - Timestamped Outputs]
  H --> K
  J --> K

  K --> L[Google Cloud Run - Serverless Compute]

