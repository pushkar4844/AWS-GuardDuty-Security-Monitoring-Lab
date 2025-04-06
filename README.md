# 🛡️ AWS VPC Security Lab

Build a two‑tier VPC—public bastion up front, private subnet behind it—and lock it down with Security Groups, NACLs, and Flow Logs. Hands‑on, click‑by‑click, zero fluff.

[![License](https://img.shields.io/github/license/chetflowers/AWS-VPC-Security?color=blue)](LICENSE)  
[![Last Commit](https://img.shields.io/github/last-commit/chetflowers/AWS-VPC-Security)](../../commits)

---

## 🎯 What You'll Learn
- Slice a VPC into **public** and **private** subnets  
- Pin inbound SSH to a single bastion host  
- Chain Security Groups *and* Network ACLs for layered defense  
- Turn on VPC Flow Logs and read the receipts  
- Troubleshoot “can’t SSH” and “no Internet” headaches  

---

## 🧪 Lab Tasks
- Create the VPC, subnets, route tables, and Internet Gateway  
- Launch a bastion EC2 in the public subnet and a workload EC2 in the private subnet  
- Attach an Elastic IP to the bastion  
- Test SSH: **laptop → bastion → private host**  
- Enable Flow Logs and watch traffic in CloudWatch  

---

## ⚙️ Architecture Components
- **VPC `10.0.0.0/16`** — your IP sandbox  
- **Public subnet `10.0.1.0/24`** — bastion EC2, Elastic IP, SSH allowed from your IP  
- **Private subnet `10.0.2.0/24`** — workload EC2, no direct Internet  
- **Internet Gateway** — outbound door for the bastion (add NAT if private hosts need outbound)  
- **Route table** — public subnet routes `0.0.0.0/0` to the IGW  
- **Security Groups** — bastion-sg (SSH from you) → private-sg (SSH from bastion)  
- **Network ACLs** — extra “nope” layer on the subnet edge  
- **VPC Flow Logs** — packet receipts to CloudWatch or S3  

---

## 🖼️ Screenshots

**VPC Created**  
![VPC Created](screenshots/MySecureVPCCreate.png)

**Security Group Rules**  
![Public SG](screenshots/PublicSecurityGroupCreated.png)  
![Private SG](screenshots/PrivateSecurityGroupCreated.png)

**SSH Hop Success**  
![SSH Flow](screenshots/SSHPublictoPrivateSuccess.png)

---

## 📁 Folder Structure
