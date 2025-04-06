# AWS Threat Detection Lab 🛡️

This project simulates real-world threat detection and incident response in AWS using GuardDuty, CloudTrail, Security Hub, and Lambda. 

It showcases cloud-native security monitoring, threat tracing, and auto-remediation — all documented and version-controlled to reflect best practices in detection engineering and incident response.

---

## 🎯 What You'll Learn

- Detect suspicious activity using Amazon GuardDuty
- Analyze root cause with AWS CloudTrail
- Aggregate security findings in Security Hub
- Auto-remediate specific threats using Lambda + EventBridge
- Simulate IAM and network misuse to trigger real GuardDuty alerts
- Document, troubleshoot, and visually present threat response workflows

---

## 🧱 Architecture Overview

| Component         | Purpose                                            |
|-------------------|----------------------------------------------------|
| GuardDuty         | Detects threats like Tor traffic, port scans       |
| CloudTrail        | Logs all AWS API activity                          |
| Security Hub      | Centralizes and prioritizes findings               |
| Lambda            | Responds automatically to high-severity alerts     |
| EventBridge       | Triggers Lambda functions on GuardDuty findings    |

---

## 📁 Folder Structure

AWS-GuardDuty-Security-Monitoring-Lab/
├── README.md
├── cloudformation/                  # GuardDuty setup as Infrastructure as Code
├── lambda/                          # Auto-remediation function (Python)
├── docs/
│   ├── simulate-malicious-ip-activity.md
│   ├── cloudtrail-log-analysis.md
│   └── security-hub-dashboard-guide.md

---

## 🚀 How to Run the Lab

1. Enable GuardDuty in your AWS account
2. Simulate suspicious activity (e.g., Tor IP or stolen credentials)
3. Analyze the GuardDuty findings
4. Trace the event using CloudTrail logs
5. Auto-remediate the threat using Lambda
6. View unified alerts and scores in Security Hub

All steps are documented in `/docs/`.

---

## 🧪 Simulated Threats

- Use of AWS credentials from unapproved geolocation
- EC2 instance scanning public IPs
- Root account login attempt
- Access from known Tor exit nodes

---

## 🏆 Bonus Features

- Infrastructure as Code using CloudFormation
- GitHub-tracked troubleshooting + mistakes
- Optional Terraform version (coming soon)
- Screenshots of findings + response
