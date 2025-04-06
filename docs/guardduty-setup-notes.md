# GuardDuty Setup Notes

## ✅ Enabled GuardDuty in Region: us-east-1
- S3 protection: ✅
- Malware protection: ✅
- EKS protection: ❌ (not using it right now)

Date: April 6, 2025

## 🔐 Protection Plans Enabled

As part of AWS's 30-day free trial, the following advanced detection features were enabled:

- ✅ S3 Protection
- ✅ Malware Protection for EC2
- ✅ EKS Audit Log Monitoring
- ✅ RDS Login Activity Monitoring
- ✅ Lambda Network Activity Monitoring
- ✅ Unlimited Threat Detection

These layers enhance the lab's realism and demonstrate extended GuardDuty capabilities beyond baseline detection.

## 🖼️ Screenshots: GuardDuty Setup & Protections

![GuardDuty Enabled](../screenshots/guardduty-enabled.png)  
*GuardDuty successfully enabled in us-east-1*

![S3 Protection](../screenshots/guardduty-s3-protection.png)  
*S3 data event protection enabled*

![Malware Protection for EC2](../screenshots/guardduty-mp4ec2-protection.png)  
*Malware protection for EC2 instances*

![EKS Protection](../screenshots/guardduty-eks-protection.png)  
*Audit log monitoring for Kubernetes (EKS)*

![RDS Protection](../screenshots/guardduty-rds-protection.png)  
*RDS login activity monitoring enabled*

![Lambda Protection](../screenshots/guardduty-lambda-protection.png)  
*Lambda network activity monitoring enabled*

![Extended Threat Detection](../screenshots/guardduty-etd-protection.png)  
*Advanced threat detection features enabled*

![IAM User Config](../screenshots/iam-user-config.png)  
*IAM user with programmatic access for lab*

![IAM Group Policies](../screenshots/iam-group-policies.png)  
*GuardDuty permissions assigned via group*
