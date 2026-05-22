import streamlit as st
import pandas as pd
import os
from sklearn.ensemble import IsolationForest

st.set_page_config(page_title="STAR Log Analyzer", layout="wide")

st.title(" STAR  Log Analyzer (ML-Based SOC System)")
st.write("Upload log file to detect anomalies and classify IP behavior")

storage_file = "all_logs.csv"


file = st.file_uploader("Upload CSV Log File", type=["csv"])
if file is not None:

    df = pd.read_csv(file)

    # Ensure required columns exist
    if not {"IP", "Time", "Action", "Status"}.issubset(df.columns):
        st.error("CSV must contain: IP, Time, Action, Status columns")
        st.stop()
        
    if os.path.exists(storage_file):
        old = pd.read_csv(storage_file)
        df = pd.concat([old, df], ignore_index=True)

    df.to_csv(storage_file, index=False)

    st.subheader("Full Log Data")
    st.dataframe(df)

   
    df["failed_flag"] = df["Status"].apply(lambda x: 1 if str(x).lower() == "failed" else 0)

    features = df.groupby("IP").agg({
        "failed_flag": "sum",
        "Action": "count"
    }).reset_index()

    features.columns = ["IP", "Failed_Count", "Total_Activity"]

   
    model = IsolationForest(contamination=0.2, random_state=42)

    features["Anomaly"] = model.fit_predict(
        features[["Failed_Count", "Total_Activity"]]
    )

   
    features["Risk_Score"] = (
        features["Failed_Count"] * 10 +
        features["Total_Activity"] * 2
    )

    # Normalize risk score
    max_score = features["Risk_Score"].max()
    if max_score != 0:
        features["Risk_Score"] = (features["Risk_Score"] / max_score) * 100

    
    def classify(row):
        return "REJECTED" if row["Anomaly"] == -1 else "ACCEPTED"

    features["Status"] = features.apply(classify, axis=1)

    
    def confidence(row):
        if row["Status"] == "REJECTED":
            return "High Risk"
        elif row["Risk_Score"] > 60:
            return "Medium Risk"
        else:
            return "Low Risk"

    features["Confidence"] = features.apply(confidence, axis=1)

  
    st.subheader("Analysis Results")
    st.dataframe(features)

  
    st.subheader("Security Alerts")

    rejected = features[features["Status"] == "REJECTED"]

    if rejected.empty:
        st.success("No major threats detected")
    else:
        for _, row in rejected.iterrows():
            st.error(
                f"IP {row['IP']} REJECTED | "
                f"Risk Score: {row['Risk_Score']:.2f} | "
                f"{row['Confidence']}"
            )

    st.subheader("Accepted IPs (Safe Traffic)")
    accepted = features[features["Status"] == "ACCEPTED"]
    st.dataframe(accepted)