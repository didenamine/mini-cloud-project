🚀 Mini Cloud Project – Microservices Platform



📌 Overview

This project implements a containerized microservices architecture using Docker and Docker Compose.

It demonstrates:

-Scalable backend services

-Reverse proxy with load balancing

-Database persistence

-Caching

-Monitoring

-CI/CD automation


🧱 Architecture

The system follows a multi-layer microservices architecture:

User → Nginx (HTTP) → Flask Apps (scaled) → MySQL + Redis
                                   ↓
                               cAdvisor

⚙️ Tech Stack

Backend: Flask (Python)

Reverse Proxy: Nginx

Database: MySQL

Cache: Redis

Monitoring: cAdvisor

CI/CD: GitHub Actions

Containerization: Docker & Docker Compose


🧩 Services

🔹 Flask API

REST API for task management

Endpoints:

GET /tasks

POST /tasks

DELETE /tasks/<id>

Horizontally scalable


🔹 Nginx



Load balancing across multiple app instances




🔹 MySQL
Persistent storage using Docker volumes

🔹 Redis

Caching layer

Improves performance and reduces DB load

🔹 cAdvisor

Container monitoring

Tracks:

CPU usage

Memory usage

Network activity




📦 Volumes

db-data: persists MySQL data

Ensures data durability across container restarts


🌐 Networking

All services communicate via Docker network

Service discovery via container names:

app → db

app → redis

nginx → app


📈 Scalability

The application supports horizontal scaling:

docker compose up -d --scale app=2

Nginx distributes traffic across instances

Improves availability and performance


🔄 CI/CD Pipeline

Implemented using GitHub Actions:


Steps:

Build Docker images

Push to Docker Hub

Deploy with Docker Compose

Run API tests (GET, POST, DELETE)

Validate system health


🧪 API Testing

Automated tests using curl:


Validate endpoints

Ensure service availability

Fail pipeline if errors occur


📊 Monitoring

Access cAdvisor locally:

http://localhost:8080

Provides real-time metrics for all containers.



🚀 How to Run

docker compose up -d --build --scale app=2


📁 Project Structure

mini-cloud-project/

│

├── app/

├── nginx/

├── docker-compose.yml

├── .github/workflows/

└── README.md

🎯 Key Features

✅ Microservices architecture

✅ Load balancing (Nginx)

✅ HTTP support

✅ Persistent database

✅ Redis caching

✅ Monitoring (cAdvisor)

✅ CI/CD pipeline

✅ Horizontal scaling



💡 Future Improvements

Add Prometheus + Grafana dashboards

Implement JWT authentication

Deploy to AWS / Azure

Replace Nginx with Traefik (auto HTTPS)


👨‍💻 Author

Amine Diden
