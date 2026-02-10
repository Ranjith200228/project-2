# ⭐ Cloud Conversational AI Platform  
### Production-Grade Speech Intelligence System (GCP • Cloud Run • AI APIs)

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-Production-black)
![Google Cloud](https://img.shields.io/badge/Google%20Cloud-Run-success)
![Docker](https://img.shields.io/badge/Containerized-Yes-blueviolet)
![Architecture](https://img.shields.io/badge/Design-Cloud--Native-orange)

---

## 🚀 Live Production Demo

👉 **Launch the Application:**  
### **<CLOUD_RUN_URL;https://console.cloud.google.com/run/detail/us-east1/project2/metrics?hl=en&inv=1&invt=Abqn8Q&project=convai-449103>**
### **<app_url; https://project2-610853696776.us-east1.run.app/>**
*(Fully deployed serverless AI system — no local setup required.)*

---

## 🧠 Executive Summary

This repository contains a **production-style Conversational AI platform** engineered to process human speech, understand emotional tone, and generate natural voice responses — all delivered through a scalable serverless infrastructure.

The system integrates multiple Google Cloud AI services into a cohesive microservice architecture capable of supporting real-world conversational workloads.

> **Primary Goal:** Demonstrate the design, development, and deployment of an end-to-end cloud-native AI application.

---


### This project goes further — showcasing **production engineering capabilities**:

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

A[Client Browser] --> B[MediaRecorder API<br>(Audio Capture)]
B --> C[Frontend<br>(HTML + JavaScript)]
C --> D[Flask REST API<br>(Docker Container)]

D --> E[Google Speech-to-Text]
E --> F[Transcript]

D --> G[Google Natural Language API]
G --> H[Sentiment Score]

D --> I[Google Text-to-Speech]
I --> J[Synthesized Audio]

F --> K[Artifact Storage<br>(Timestamped Outputs)]
H --> K
J --> K

K --> L[Google Cloud Run<br>(Serverless Compute)]
----

### 😊 Real-Time Sentiment Intelligence

Automatically evaluates emotional tone:

| Score | Interpretation |
|--------|----------------|
| > 0 | Positive |
| = 0 | Neutral |
| < 0 | Negative |

Simulates enterprise conversational analytics workflows used in:

- Customer support AI  
- Voice assistants  
- Contact center intelligence  

---

### 🔊 Neural Text-to-Speech Engine

Transforms written text into natural audio:

✔ Human-like speech synthesis  
✔ Downloadable audio files  
✔ Bidirectional conversational capability  

---

### ☁️ Serverless Cloud Deployment

The platform runs entirely on **Google Cloud Run**, enabling:

- Automatic scaling  
- Zero infrastructure management  
- High availability  
- Cost-efficient compute  

---

## 🧰 Technology Stack

### Languages
- Python  
- JavaScript  

### Backend
- Flask REST API  
- Stateless service design  

### Cloud & AI
- Google Cloud Run  
- Speech-to-Text API  
- Natural Language API  
- Text-to-Speech API  

### DevOps
- Docker containerization  
- Service account authentication  
- Environment-based configuration  

---

## 📂 Repository Structure
cloud-conversational-ai/
│
├── src/
│ ├── app.py
│ ├── templates/
│ ├── static/
│ └── utils/
│
├── storage/ # ignored (generated artifacts)
├── Dockerfile
├── requirements.txt
└── README.md


Designed to mirror **industry backend standards** for scalability and maintainability.

---

## ⚙️ Run Locally (Developer Setup)

### 1️⃣ Requirements
- Python 3.10+
- Google Cloud Project
- Enabled APIs:
  - Speech-to-Text  
  - Natural Language  
  - Text-to-Speech  

---

### 2️⃣ Authenticate

```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/service-account.json"

### Windows (PowerShell):
setx GOOGLE_APPLICATION_CREDENTIALS "path\to\service-account.json"

### 3️⃣ Install Dependencies
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements.txt

### 4️⃣ Start the Server
python src/app.py

### 🐳 Production Deployment
##  Build Container
gcloud builds submit --tag gcr.io/<PROJECT_ID>/conversational-ai

### Deploy to Cloud Run
gcloud run deploy conversational-ai \
  --image gcr.io/<PROJECT_ID>/conversational-ai \
  --platform managed \
  --region us-east1 \
  --allow-unauthenticated
## Cloud Run automatically provisions HTTPS and load balancing.


### 🔗 API Surface
Endpoint	Method	Purpose
/	GET	UI + artifact listing
/upload	POST	Audio → transcription + sentiment
/upload_text	POST	Text → speech
/uploads/<file>	GET	Retrieve audio
/results/<file>	GET	Retrieve outputs

### 📊 Production Engineering Considerations
This system is intentionally designed with extensibility in mind.

### Immediate Enterprise Upgrades
✅ Migrate artifacts → Google Cloud Storage
✅ Introduce Pub/Sub for async processing
✅ Add IAM-based authentication
✅ Implement rate limiting
✅ Enable Cloud Monitoring
✅ Build CI/CD pipeline

These enhancements would evolve the system into a fully enterprise-ready conversational intelligence platform.

### 🎯 Engineering Competencies Demonstrated
This project showcases my ability to:

✔ Architect end-to-end AI platforms
✔ Deploy cloud-native ML systems
✔ Integrate production APIs
✔ Containerize backend services
✔ Design scalable microservices
✔ Apply modern DevOps practices

