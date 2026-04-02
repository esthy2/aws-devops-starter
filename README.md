# 🚀 AWS DevOps Starter Project

## 📌 Overview

This project demonstrates a complete **DevOps workflow** using:

* **Terraform** to provision AWS infrastructure
* **EC2** as a Docker host
* **Docker & Docker Compose** to run containers
* **Prometheus & Grafana** for monitoring
* **GitHub Actions** for CI/CD pipeline
* **Docker Hub** for image storage

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
```

---

## 📂 Project Structure

```
aws-devops-starter/
├── terraform/
├── app/
├── monitoring/
├── .github/workflows/
└── README.md
```

---

## ⚙️ Prerequisites

* AWS account
* Terraform installed
* Git installed
* Docker Hub account
* GitHub account
* Existing AWS key pair

---

## 🚀 Deployment Steps

### 1. Provision Infrastructure

```bash
cd terraform
terraform init
terraform apply
```

---

### 2. SSH into EC2

```bash
ssh -i /path/to/your-key.pem ec2-user@<EC2_PUBLIC_IP>
```

---

### 3. Deploy Containers

```bash
cd /home/ec2-user/aws-devops-starter/monitoring
docker compose up -d --build
```

---

## 🌐 Access Services

| Service    | URL                         |
| ---------- | --------------------------- |
| App        | http://<EC2_PUBLIC_IP>:5000 |
| Prometheus | http://<EC2_PUBLIC_IP>:9090 |
| Grafana    | http://<EC2_PUBLIC_IP>:3000 |

---

## 🔐 Security Notes

* Do NOT commit `.pem` files
* Use `.gitignore` to exclude sensitive files
* Restrict SSH access using your public IP

---

## 🔄 CI/CD Pipeline

GitHub Actions will:

1. Build Docker image
2. Scan image using Trivy
3. Push image to Docker Hub

Trigger: push to `main` branch

---

## 🐳 Docker Image

Image is pushed to:

```
docker.io/<your-dockerhub-username>/aws-devops-starter:latest
```

---

## 🧪 Monitoring

* Prometheus collects metrics from the app
* Grafana visualizes metrics

---

## 🧹 Cleanup

```bash
cd terraform
terraform destroy
```

---

## 🎯 Outcome

This project demonstrates:

* Infrastructure as Code (Terraform)
* Containerized application deployment
* Monitoring with Prometheus & Grafana
* CI/CD automation with GitHub Actions

---

## 👩‍💻 Author

Built by Esther 🚀
