import streamlit as st
import numpy as np

# Page configuration
st.set_page_config(page_title="NRS-ILD Risk Calculator", page_icon="🫁", layout="centered")

st.title("🫁 NRS-ILD Risk Calculator")
st.markdown("A pragmatic triage tool for disease severity stratification in interstitial lung disease, based on the NRS-ILD score.")
st.markdown("---")

# Input fields
col1, col2, col3 = st.columns(3)

with col1:
    fvc = st.number_input("FVC (% predicted)", min_value=0, max_value=150, value=80, step=1)
with col2:
    walk_distance = st.number_input("6MWD (meters)", min_value=0, max_value=800, value=400, step=10)
with col3:
    borg = st.number_input("Borg Dyspnea Score", min_value=0.0, max_value=10.0, value=2.0, step=0.5)

st.markdown("---")

# Calculation Logic
if st.button("Calculate Risk Tier", use_container_width=True):
    score = 0
    
    # FVC Scoring
    if fvc < 50:
        score += 2
    elif fvc <= 74:
        score += 1
        
    # 6MWD Scoring
    if walk_distance < 250:
        score += 2
    elif walk_distance <= 349:
        score += 1
        
    # Borg Scoring
    if borg >= 5:
        score += 2
    elif borg >= 3:
        score += 1
        
    # Output Display
    st.subheader(f"Total NRS-ILD Score: {score} / 6")
    
    if score >= 4:
        st.error("High Risk (Severe Disease Impairment) \n\nConsider urgent therapeutic escalation or tertiary referral.")
    elif score >= 2:
        st.warning("Moderate Risk (Moderate Disease Impairment) \n\nMonitor closely and evaluate for progression.")
    else:
        st.success("Low Risk (Mild Disease Impairment) \n\nContinue standard maintenance and monitoring.")
        
st.markdown("---")
st.caption("Disclaimer: This tool calculates the NRS-ILD score as described by Moulik et al., 2026. It is designed as a triage aid and does not substitute for comprehensive clinical judgment or formal physiological testing. No patient data is stored or transmitted by this application.")
