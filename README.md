🛡️ AI Credential Stuffing Detection System

Real-Time Behavioral Risk Engine for Authentication Security

🚀 Overview

This project is a real-time AI-powered Security Operations Console (SOC) designed to detect and mitigate credential stuffing attacks using behavioral risk scoring.

It simulates authentication telemetry, evaluates risk using a custom ML-based engine, and logs threat intelligence to Supabase for persistent monitoring.

The system dynamically classifies authentication attempts as:

✅ ALLOW

🔐 MFA (Multi-Factor Authentication Required)

🚫 BLOCK

🔍 Problem Statement

Credential stuffing attacks exploit reused credentials at scale.

Traditional rule-based systems fail to adapt to evolving attack patterns.

This project demonstrates how behavioral features and risk scoring can:

Detect anomalous login activity

Identify impossible travel patterns

Block automated intrusion attempts

Provide live threat visualization

🧠 Architecture

User Input (Telemetry)
⬇
Feature Builder
⬇
Risk Engine (ML Scoring)
⬇
Decision Engine (ALLOW / MFA / BLOCK)
⬇
Supabase Logging
⬇
Live SOC Dashboard (Streamlit)

📊 Behavioral Features Used

Login attempts per minute

Failure ratio

IP volatility

Device switching frequency

Geo-location deviation (km)

Impossible travel detection

🛠️ Tech Stack

Frontend:

Streamlit

Matplotlib

Pandas

Backend Logic:

Custom Risk Engine

Feature Engineering Module

Scikit-learn

Database:

Supabase (PostgreSQL backend)

Deployment:

Render (Cloud Hosting)

📁 Project Structure
App/
    app.py
Database/
    supabase_client.py
risk_engine/
    risk_scoring.py
Utils/
    feature_builder.py
Model/
Data/
requirements.txt
runtime.txt
⚙️ Local Setup

Clone repository:

git clone https://github.com/Jeff404-notfound/ai-credential-stuffing-detector.git
cd ai-credential-stuffing-detector

Create virtual environment:

python -m venv venv
source venv/bin/activate   # mac/linux
venv\Scripts\activate      # windows

Install dependencies:

pip install -r requirements.txt

Add environment variables:

SUPABASE_URL=your_project_url
SUPABASE_KEY=your_publishable_key

Run:

streamlit run App/app.py
🌐 Deployment (Render)

Runtime: Python 3.10.13

Build Command:

pip install -r requirements.txt

Start Command:

streamlit run App/app.py --server.port $PORT --server.address 0.0.0.0

Environment Variables required:

SUPABASE_URL

SUPABASE_KEY

PYTHON_VERSION=3.10.13

📈 Key Highlights

Real-time threat detection simulation

Live dashboard auto-refresh

Persistent event logging

Risk threshold tuning

Attack injection simulation

Clean modular architecture

🔒 Security Considerations

Uses Supabase publishable key (no service_role exposed)

Environment variables managed securely

No hardcoded secrets in repository

🎯 Future Improvements

Replace simulated telemetry with real authentication logs

Integrate anomaly detection model (Isolation Forest / XGBoost)

Add rate limiting module

Deploy backend as FastAPI microservice

Add JWT-based authentication

👨‍💻 Author

Jeff Franco
AI | Backend | Security Systems