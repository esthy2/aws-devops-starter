# 🚀 AWS DevOps Starter Platform

## 📌 Overview

This project demonstrates a **complete end-to-end DevOps workflow**, from infrastructure provisioning to deployment, monitoring, and CI/CD automation.

It showcases how to:

* Provision infrastructure using **Terraform**
* Deploy a containerized application on **AWS EC2**
* Manage services using **Docker Compose**
* Implement **CI/CD pipelines** using GitHub Actions
* Push container images to **Docker Hub**
* Monitor applications using **Prometheus & Grafana**
* Build a **custom web UI** for service visibility

---

## 🏗️ Architecture

```
Local Machine (VS Code)
        │
        │ Terraform
        ▼
AWS EC2 Instance
        │
        │ Docker + Docker Compose
        ▼
Containers:
- Flask App (5000)
- Prometheus (9090)
- Grafana (3000)

CI/CD Flow:
GitHub → GitHub Actions → Docker Hub → EC2 → Running Containers
```

---

## 📂 Project Structure

```
aws-devops-starter/
├── terraform/                # Infrastructure provisioning
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── userdata.sh
│
├── app/                      # Flask application
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── monitoring/               # Observability stack
│   ├── docker-compose.yml
│   ├── prometheus.yml
│   └── grafana/
│
├── .github/workflows/        # CI/CD pipeline
│   └── ci.yml
│
└── README.md
```

---

## ⚙️ Prerequisites

Before starting, ensure you have:

* AWS account
* Terraform installed
* Git installed
* Docker Hub account
* GitHub account
* Existing AWS EC2 Key Pair

---

## 🚀 Step-by-Step Deployment Guide

### 🔹 Step 1: Clone Repository

```bash
git clone https://github.com/<your-username>/aws-devops-starter.git
cd aws-devops-starter
```

---

### 🔹 Step 2: Configure Terraform Variables

Create a `terraform.tfvars` file:

```hcl
key_name = "your-keypair-name"
my_ip    = "your-public-ip/32"
```

📌 Notes:

* `key_name` = AWS key pair name (NOT the .pem file)
* `my_ip` = your public IP address (for SSH access restriction)

---

### 🔹 Step 3: Provision Infrastructure

```bash
cd terraform
terraform init
terraform apply
```

Confirm with:

```text
yes
```

---

### 🔹 Step 4: Get EC2 Public IP

Terraform will output your instance IP:

```text
ec2_public_ip = <EC2_PUBLIC_IP>
```

---

### 🔹 Step 5: Connect to EC2

```bash
ssh -i /path/to/your-key.pem ec2-user@<EC2_PUBLIC_IP>
```

---

### 🔹 Step 6: Copy Project Files to EC2

From your **local machine**:

```bash
scp -i /path/to/your-key.pem -r app monitoring ec2-user@<EC2_PUBLIC_IP>:/home/ec2-user/aws-devops-starter/
```

---

### 🔹 Step 7: Deploy Containers

SSH into EC2 and run:

```bash
cd /home/ec2-user/aws-devops-starter/monitoring
docker compose up -d --build
```

---

### 🔹 Step 8: Access Services

| Service    | URL                         |
| ---------- | --------------------------- |
| App        | http://<EC2_PUBLIC_IP>:5000 |
| Prometheus | http://<EC2_PUBLIC_IP>:9090 |
| Grafana    | http://<EC2_PUBLIC_IP>:3000 |

---

## 🔄 CI/CD Pipeline (GitHub Actions)

Pipeline automatically runs on:

```text
push to main branch
```

### Pipeline Stages:

1. Build Docker image
2. Scan image using Trivy
3. Push image to Docker Hub

---

## 🔐 GitHub Secrets Required

Set these in your repository:

* `DOCKERHUB_USERNAME`
* `DOCKERHUB_TOKEN`

---

## 🐳 Docker Image

Image is published to:

```
docker.io/<your-dockerhub-username>/aws-devops-starter:latest
```

---

## 🧪 Monitoring Stack

* **Prometheus** collects metrics from the Flask app
* **Grafana** visualizes metrics dashboards

---

## 🎨 Custom UI Enhancement

The application UI was upgraded from plain text to a full HTML interface.

📌 Key features:

* Responsive layout
* Service overview cards
* Monitoring links
* Request counter (dynamic)

---

## ⚠️ Troubleshooting Guide

### ❌ Issue: UI changes not reflecting

**Cause:** EC2 still has old code

**Fix:**

```bash
scp -i /path/to/key.pem app/app.py ec2-user@<EC2_PUBLIC_IP>:/home/ec2-user/aws-devops-starter/app/app.py
```

Then rebuild:

```bash
docker compose down
docker compose up -d --build
```

---

### ❌ Issue: `docker compose pull` fails

**Cause:** Wrong directory

**Fix:**

```bash
cd /home/ec2-user/aws-devops-starter/monitoring
```

---

### ❌ Issue: GitHub Actions build fails (Trivy)

**Cause:** outdated action version

**Fix:**
Update:

```yaml
uses: aquasecurity/trivy-action@0.35.0
```

---

### ❌ Issue: Changes not in GitHub

**Cause:** Changes made locally or on EC2 but not pushed

**Fix:**

```bash
git add .
git commit -m "update"
git push origin main
```

---

### ❌ Issue: Permission denied (SSH)

**Fix:**

```bash
chmod 400 your-key.pem
```

---

## 🔐 Security Best Practices

* Do NOT commit `.pem` files
* Use `.gitignore`
* Use GitHub Secrets for credentials
* Restrict SSH to your IP only

---

## 🧹 Cleanup (IMPORTANT)

To avoid AWS charges:

```bash
cd terraform
terraform destroy
```

---

## 🎯 Key Learning Outcomes

This project demonstrates:

* Infrastructure as Code (Terraform)
* Containerization (Docker)
* Multi-service orchestration (Docker Compose)
* CI/CD automation (GitHub Actions)
* Container security scanning (Trivy)
* Monitoring (Prometheus & Grafana)
* Real-world debugging and troubleshooting

---

## 👩‍💻 Author

Built with ❤️ by Esther
Cloud • DevOps • Kubernetes • AWS
