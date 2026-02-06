 🛡️ AI Credential Stuffing Attack Detection System

An AI-powered Security Operations Console (SOC) prototype that detects credential stuffing attacks using behavioral anomaly detection, adaptive risk scoring, and real-time cloud telemetry.

Built to simulate enterprise-grade authentication threat monitoring.



 🚨 Problem Statement

Credential stuffing is one of the fastest-growing cyber threats, where attackers use stolen username-password pairs to gain unauthorized access.

Traditional rule-based systems struggle to detect evolving attack patterns.

This project leverages **Artificial Intelligence** to analyze authentication behavior and proactively block suspicious login attempts.


 ⭐ Key Features

✅ AI-driven anomaly detection  
✅ Adaptive authentication (Allow / MFA / Block)  
✅ Real-time threat scoring (0–100 risk index)  
✅ Impossible travel detection  
✅ Cloud-based telemetry storage (Supabase)  
✅ Live SOC dashboard  
✅ Attack simulation engine  
✅ Threat escalation visualization  
✅ Security event logging  



 🧠 Architecture Overview

Authentication Signals
↓
Feature Engineering
↓
Isolation Forest (AI Engine)
↓
Risk Scoring System
↓
Adaptive Decision Engine
↓
Supabase Cloud Database
↓
Live SOC Dashboard

yaml


 🤖 Where AI is Used

The system uses **Isolation Forest**, an unsupervised machine learning algorithm, to detect anomalies in authentication behavior.

Unlike rule-based systems, this allows detection of:

- Zero-day attacks  
- Bot-driven login bursts  
- Behavioral deviations  
- Automated credential stuffing  



 ⚙️ Tech Stack

 AI / ML
- Python  
- Scikit-learn  
- Isolation Forest  

 Data Processing
- Pandas  
- NumPy  

Cloud & Database
- Supabase  
- PostgreSQL  

 Visualization
- Streamlit  
- Matplotlib  



 📊 Risk Model

| Risk Score | Action |
|--------|------------|
| 0–30 | Allow Login |
| 30–70 | Trigger MFA |
| 70+ | Block Attempt |



 🔐 Security Concepts Implemented

- Behavioral Authentication  
- Adaptive Access Control  
- Threat Telemetry  
- Anomaly Detection  
- SOC Monitoring  
- Impossible Travel Detection  



🚀 How to Run Locally

 1️⃣ Clone the repository

```bash
git clone https://github.com/Jeff404-notfound/ai-credential-stuffing-detector.git
