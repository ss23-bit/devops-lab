# 🚀 High-Availability DevOps & AI Lab

This is my central command center for mastering production-grade infrastructure. It features a high-availability microservice cluster, Infrastructure as Code (IaC), and an automated AI-driven security gateway.

## 💼 Professional Impact (The "Hire Me" Section)
*The following technical achievements were architected, tested, and validated in this environment:*

* **Architected and provisioned** a high-availability, load-balanced web cluster using Nginx, Docker Compose, and Gunicorn, capable of zero-downtime horizontal scaling.
* **Engineered an automated CI/CD pipeline** via GitHub Actions to facilitate continuous integration, testing, and automated deployment to AWS EC2 environments.
* **Integrated Generative AI (Google GenAI)** directly into the CI pipeline to act as an automated security gatekeeper, actively auditing Dockerfiles for vulnerabilities and root-user anti-patterns.
* **Implemented Infrastructure as Code (IaC)** using Terraform to dynamically provision and manage AWS compute resources and security groups, eliminating manual configuration drift.
* **Enforced immutable infrastructure** and security best practices by utilizing slim container base images, non-root execution, and automated user-data bootstrapping scripts.

---

## 🌟 Featured Project: Scalable Python Cluster
*A production-ready architecture designed for security and scale.*

### 🏗️ Architecture
- **Infrastructure:** AWS EC2 provisioned via **Terraform**.
- **Reverse Proxy:** Nginx (Acts as a Layer 7 Load Balancer).
- **App Stack:** Flask + Gunicorn (Multi-worker for high throughput).
- **Security:** Custom AI Auditor powered by **Google Gemini** (Integrated via GitHub Actions).
- **Orchestration:** Docker Compose with automated health checks.

### 🚀 Key Capabilities
- **Self-Healing:** Docker health checks automatically detect and bypass unhealthy containers.
- **Instant Scaling:** Supports horizontal scaling with a single command: `docker compose up -d --scale web-app=3`
- **AI Governance:** Every commit is audited for security anti-patterns by an LLM-based gatekeeper before it ever touches production.

---

## 🗺️ Mastery Roadmap (Current Focus: The Second Run)
*After reaching a full cloud deployment in 37 days, I am restarting for deep mastery of the fundamentals.*

- [ ] **Phase 1: Linux & Networking** (Advanced CLI, SSH Key Management, TCP/IP)
- [ ] **Phase 2: Docker Orchestration** (Multi-stage builds, non-root users, Healthchecks)
- [ ] **Phase 3: Cloud & IaC** (Terraform State Management, AWS Security Groups, CI/CD)

## 📁 Repository Structure
- `app-cluster/`: Production Nginx/Flask/Gunicorn configuration.
- `ai-auditor/`: Gemini-powered security auditing logic.
- `terraform-lab/`: IaC scripts for AWS provisioning.
- `01-linux-basics/`: Shell scripts and CLI proficiency practice.
- `99-notes/`: Daily learning logs.

## 🛠️ Tech Stack
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)