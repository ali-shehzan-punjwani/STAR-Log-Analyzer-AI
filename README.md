# STAR Log Analyzer – AI & Machine Learning SOC System

\
\
\
\


---

# 📌 Project Overview

STAR Log Analyzer is an AI-powered cybersecurity log analysis and threat detection system developed using Python, Streamlit, and Machine Learning.

The project simulates a real-world Security Operations Center (SOC) environment by analyzing network logs, detecting suspicious activities, classifying risky IP addresses, and generating security alerts.

The system combines:

- Rule-Based Threat Detection
- Machine Learning Anomaly Detection
- Behavioral Analysis
- Risk Classification

This hybrid detection approach improves the accuracy of identifying malicious activities such as brute-force attacks, suspicious logins, bot activity, and abnormal traffic behavior.

---

# 🎯 Objectives

The main objective of this project is to design and implement an intelligent cybersecurity monitoring system capable of:

- Automatically analyzing log files
- Detecting suspicious network behavior
- Identifying abnormal IP activities
- Performing anomaly detection using AI/ML
- Generating real-time security alerts
- Simulating SOC-based threat analysis

---

# 🚀 Features

## ✅ Rule-Based Threat Detection

The system uses predefined cybersecurity logic to identify known attack patterns.

### Detects:

- Brute-force login attacks
- Multiple failed login attempts
- Suspicious login behavior
- Unknown IP activities
- Rapid bot-like requests
- High traffic anomalies

---

## 🤖 Machine Learning Anomaly Detection

The project uses the Isolation Forest algorithm from Scikit-learn for anomaly detection.

Machine learning helps identify:

- Hidden threats
- Unknown attack patterns
- Abnormal IP behavior
- Unusual traffic activity

This makes the system more intelligent compared to traditional rule-only detection systems.

---

## 📊 Risk Classification System

Each IP address is analyzed and assigned a risk score.

### Risk Levels:

- 🟢 Low Risk
- 🟡 Medium Risk
- 🟠 High Risk
- 🔴 Critical Risk

The classification is based on:

- Failed login attempts
- Total activity count
- Behavioral patterns
- ML anomaly detection results

---

# 🛠️ Technologies Used

| Technology       | Purpose                     |
| ---------------- | --------------------------- |
| Python           | Core Programming Language   |
| Streamlit        | Web Dashboard Interface     |
| Pandas           | Data Processing & Analysis  |
| Scikit-learn     | Machine Learning            |
| Isolation Forest | Anomaly Detection Algorithm |
| NumPy            | Numerical Operations        |

---

# 🧠 Machine Learning Model

## Isolation Forest Algorithm

Isolation Forest is an unsupervised machine learning algorithm used for anomaly detection.

It works by:

- Isolating unusual data points
- Detecting abnormal behavior
- Identifying suspicious activities without labeled data

### Why Isolation Forest?

- Fast and efficient
- Works well for cybersecurity anomaly detection
- Suitable for large log datasets
- Detects unknown attacks

---

# 📂 Input Dataset

The system accepts CSV log files containing:

| Field      | Description            |
| ---------- | ---------------------- |
| IP Address | Source IP              |
| Timestamp  | Activity Time          |
| Action     | Login / Request / Scan |
| Status     | Success or Failure     |

---

# ⚙️ System Workflow

## Step 1 — Upload Log File

The user uploads a CSV log dataset through the Streamlit dashboard.

## Step 2 — Data Processing

The system reads and organizes data using Pandas.

## Step 3 — Feature Extraction

Behavioral features are extracted for each IP address.

## Step 4 — Rule-Based Analysis

Known cyber attack patterns are detected.

## Step 5 — ML Anomaly Detection

Isolation Forest identifies abnormal behavior.

## Step 6 — Risk Scoring

Risk scores are calculated based on suspicious activities.

## Step 7 — Threat Classification

IPs are classified into risk categories.

## Step 8 — Dashboard Output

Results are displayed visually on the dashboard.

---

# 📈 Threats Detected

The system successfully identifies:

- Brute-force attacks
- Suspicious login attempts
- High traffic anomalies
- Bot-like rapid requests
- Abnormal network activity
- Unknown malicious IP behavior

---

# 🖥️ Streamlit Dashboard

The dashboard provides:

- Uploaded log visualization
- IP-wise analysis
- Threat alerts
- Risk classification tables
- Machine learning results
- Safe IP monitoring

---

# 📁 Project Structure

```bash
STAR-Log-Analyzer/
│
├── advance.py
├── requirements.txt
├── README.md
├── network_log.csv
|──star_analyzer_log_dataset.csv  
└── dataset/
    └── logs.csv
```

---

# 🔧 Installation & Setup

## Clone Repository

```bash
git clone https://github.com/your-username/star-log-analyzer-ai.git
```

## Open Project Folder

```bash
cd star-log-analyzer-ai
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Streamlit Application

```bash
streamlit run app.py
```

---

# 📦 Requirements

```txt
streamlit
pandas
numpy
scikit-learn
```

---

# 📊 Example Attack Scenarios

The dataset contains simulated cybersecurity attacks such as:

- Failed login attempts
- Brute-force behavior
- Rapid bot requests
- Suspicious scanning activity
- Normal user traffic

This helps evaluate the effectiveness of the detection engine.

---

# 🔍 Analysis & Results

The system analyzes each IP individually using:

- Rule-based detection
- Behavioral monitoring
- AI anomaly detection

### Results:

✅ Successfully identifies suspicious IPs  
✅ Detects anomalies using ML  
✅ Classifies risks accurately  
✅ Generates threat alerts  
✅ Simulates real SOC analysis workflow

---

# 💡 Future Improvements

Future enhancements may include:

- Real-time log streaming
- Deep Learning integration
- Threat Intelligence APIs
- SIEM integration
- Cloud deployment
- Advanced visualization dashboard
- Real-time notification system

---

# 📚 Learning Outcomes

Through this project, the following concepts were implemented:

- Cybersecurity Monitoring
- SOC Operations
- AI-Based Threat Detection
- Machine Learning for Security
- Anomaly Detection
- Streamlit Dashboard Development
- Data Analysis using Pandas

---

# 📖 References

- NIST Cybersecurity Framework
- Scikit-learn Documentation
- Streamlit Documentation
- Pandas Documentation
- Network Security Essentials — William Stallings

---

# ⭐ GitHub Topics

cybersecurity • machine-learning • streamlit • python • anomaly-detection • soc • siem • ai-security • isolation-forest

---

# 📫 Contact

**Ali Shehzan Punjwani**  
🎓 BSCS Student @ Iqra University  
📍 Karachi, Pakistan  
📧 shehzansohail5637@gmail.com  
🔗 https://www.linkedin.com/in/ali-shehzan-punjwani/
