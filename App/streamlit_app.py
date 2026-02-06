import sys
import os
import time
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# ✅ NEW — Live refresh
from streamlit_autorefresh import st_autorefresh

from Database.supabase_client import supabase
from risk_engine.risk_scoring import RiskEngine
from Utils.feature_builder import FeatureBuilder


# -------------------------------------------------
# LOAD ENGINES
# -------------------------------------------------

engine = RiskEngine()
builder = FeatureBuilder()

st.set_page_config(
    page_title="SOC Credential Threat Monitor",
    layout="wide"
)

# ✅ NEW — LIVE REFRESH (5 seconds)
st_autorefresh(interval=5000, key="live_soc")

st.title("🛡️ Security Operations Console")
st.caption("AI-Powered Authentication Threat Detection")


# -------------------------------------------------
# SESSION MEMORY
# -------------------------------------------------

if "security_events" not in st.session_state:
    st.session_state.security_events = []

if "threat_stats" not in st.session_state:
    st.session_state.threat_stats = {
        "safe": 0,
        "mfa": 0,
        "blocked": 0
    }


# -------------------------------------------------
# 🔥 NEW — ALWAYS SYNC WITH SUPABASE
# -------------------------------------------------

try:

    response = supabase.table("security_events")\
        .select("*")\
        .order("timestamp", desc=False)\
        .execute()

    if response.data:

        st.session_state.security_events = response.data

        # reset counters before rebuilding
        st.session_state.threat_stats = {
            "safe": 0,
            "mfa": 0,
            "blocked": 0
        }

        for event in response.data:

            decision = event["decision"]

            if decision == "ALLOW":
                st.session_state.threat_stats["safe"] += 1

            elif decision == "MFA":
                st.session_state.threat_stats["mfa"] += 1

            else:
                st.session_state.threat_stats["blocked"] += 1

except Exception as e:
    st.warning(f"Database not reachable — running in local mode. ({e})")


# -------------------------------------------------
# LIVE ALERT BANNER
# -------------------------------------------------

if st.session_state.threat_stats["blocked"] > 0:
    st.error("🚨 ACTIVE SECURITY ALERT: Malicious authentication attempts detected.")
else:
    st.success("✅ SYSTEM NORMAL — No active threats.")


# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.title("Security Controls")

if st.sidebar.button("Reset Console"):
    st.session_state.security_events = []
    st.session_state.threat_stats = {
        "safe": 0,
        "mfa": 0,
        "blocked": 0
    }

if st.button("Test Database Connection"):

    try:
        supabase.table("security_events").select("*").limit(1).execute()
        st.success("✅ Supabase Connected Successfully!")

    except Exception as e:
        st.error("❌ Supabase Connection Failed")
        st.write(e)


# -------------------------------------------------
# KPI METRICS
# -------------------------------------------------

col1, col2, col3 = st.columns(3)

col1.metric("Safe Authentications", st.session_state.threat_stats["safe"])
col2.metric("MFA Challenges", st.session_state.threat_stats["mfa"])
col3.metric("Blocked Intrusions", st.session_state.threat_stats["blocked"])

st.divider()


# -------------------------------------------------
# AUTH INPUT
# -------------------------------------------------

st.header("Authentication Telemetry Input")

login_attempts = st.slider("Login Attempts / Minute", 1, 120, 2)
failed_ratio = st.slider("Failure Ratio", 0.0, 1.0, 0.1)
ip_changes = st.slider("IP Volatility", 0, 10, 0)
device_changes = st.slider("Device Switching", 0, 5, 0)
geo_distance = st.slider("Geo Deviation (km)", 0, 15000, 10)

features = builder.build_feature_vector(
    login_attempts,
    failed_ratio,
    ip_changes,
    device_changes,
    geo_distance
)


def detect_impossible_travel(distance):
    return distance > 3000


# -------------------------------------------------
# SAFE DB INSERT
# -------------------------------------------------

def log_to_supabase(event):

    try:
        supabase.table("security_events").insert(event).execute()
        st.success("Threat logged to database ✅")

    except Exception as e:
        st.error(f"Database logging failed: {e}")


# -------------------------------------------------
# RUN THREAT ANALYSIS
# -------------------------------------------------

if st.button("Run Threat Analysis"):

    with st.spinner("Analyzing behavioral telemetry..."):
        time.sleep(1)

    result = engine.evaluate_login(features)
    risk = int(result["risk_score"])

    if detect_impossible_travel(geo_distance):
        risk = min(100, risk + 25)
        st.warning("Impossible travel signature detected.")

    timestamp = datetime.now().isoformat()

    decision = (
        "ALLOW" if risk < 30 else
        "MFA" if risk < 70 else
        "BLOCK"
    )

    event = {
        "timestamp": timestamp,
        "risk": risk,
        "decision": decision,
        "attempts": int(login_attempts),
        "failed_ratio": float(failed_ratio),
        "ip_changes": int(ip_changes),
        "device_changes": int(device_changes),
        "geo_distance": int(geo_distance)
    }

    st.session_state.security_events.append(event)

    log_to_supabase(event)

    st.subheader(f"Risk Score → {risk}")
    st.progress(risk)


# -------------------------------------------------
# ATTACK SIMULATION
# -------------------------------------------------

st.divider()
st.header("Threat Injection Engine")

if st.button("Inject Credential Stuffing Attack"):

    with st.spinner("Injecting hostile traffic..."):
        time.sleep(1)

    timestamp = datetime.now().isoformat()

    event = {
        "timestamp": timestamp,
        "risk": 95,
        "decision": "BLOCK",
        "attempts": 120,
        "failed_ratio": 0.98,
        "ip_changes": 10,
        "device_changes": 5,
        "geo_distance": 9000
    }

    st.session_state.security_events.append(event)

    log_to_supabase(event)

    st.error("CRITICAL — Automated intrusion blocked.")


# -------------------------------------------------
# 🔥 ELITE SOC GRAPH
# -------------------------------------------------

st.divider()
st.header("Threat Telemetry Trend")

if len(st.session_state.security_events) > 1:

    df = pd.DataFrame(st.session_state.security_events)

    fig, ax = plt.subplots(figsize=(13,5))

    fig.patch.set_facecolor('#111827')
    ax.set_facecolor('#111827')

    ax.plot(
        df["risk"],
        color='#00F5D4',
        linewidth=3,
        marker='o',
        markersize=5
    )

    ax.axhline(30, linestyle='--', linewidth=2, color='#22c55e', label="ALLOW")
    ax.axhline(70, linestyle='--', linewidth=2, color='#ef4444', label="BLOCK")

    ax.grid(color='gray', linestyle='--', linewidth=0.3, alpha=0.3)

    ax.tick_params(colors='white')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_color('white')
    ax.title.set_color('white')

    ax.set_title("Real-Time Threat Escalation", fontsize=15, fontweight='bold')
    ax.set_xlabel("Authentication Events")
    ax.set_ylabel("Risk Score")

    ax.legend()

    st.pyplot(fig)

else:
    st.info("Awaiting telemetry...")


# -------------------------------------------------
# 🔥 NEW — LIVE THREAT FEED
# -------------------------------------------------

st.divider()
st.header("📡 Live Security Event Feed")

if st.session_state.security_events:

    df = pd.DataFrame(st.session_state.security_events)

    st.dataframe(
        df.sort_values(by="timestamp", ascending=False),
        width="stretch"
    )

else:
    st.info("No security events recorded.")
