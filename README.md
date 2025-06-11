# 🌸 Iris Classifier API – FastAPI + Docker + GCP

## 🚀 Project Overview

This project deploys a real-time **machine learning API** to predict the species of an iris flower based on its sepal and petal measurements.

---

## 🧠 Use Case

You provide 4 features:

```json
{
  "features": [6.3, 3.3, 6.0, 2.5]
}
```

The model returns a prediction:

```json
{
  "prediction": 2
}
```

Which corresponds to: **Iris virginica**

---

## 🛠️ Tech Stack

* FastAPI (Python)
* Docker
* Google Cloud Platform (Compute Engine)
* Logistic Regression (Scikit-learn)
* systemd (for auto-restart)
* Swagger UI (`/docs`)

---

## ⚙️ Architecture

```
[FastAPI Server]  <-- Docker container
       ↓
[Prediction Logic using Scikit-learn]
       ↓
[GCP VM] <-- Exposed via port 8080
```

---

## 🏗️ GCP Infrastructure Setup

### ✅ 1. Enable GCP Services

```bash
gcloud services enable compute.googleapis.com
```

### ✅ 2. Create a GCP VM

* Name: `mlops-api-vm`
* Region: `us-central1`
* Machine type: `e2-micro`
* Boot disk: Ubuntu 22.04 LTS
* Enable HTTP and HTTPS
* Add tag: `mlops-api`

### ✅ 3. Open Port 8080

```bash
gcloud compute firewall-rules create allow-mlops-api \
  --allow=tcp:8080 \
  --target-tags=mlops-api \
  --direction=INGRESS \
  --priority=1000 \
  --network=default \
  --description="Allow traffic to FastAPI container on port 8080"
```

---

## 🔧 Local Setup & Running the App

### ✅ Train the Model

```bash
python train.py
```

### ✅ Build Docker Image

```bash
docker build -t iris-api .
```

### ✅ Run the Docker Container

```bash
docker run -d -p 8080:8080 iris-api
```

Visit: `http://<YOUR_VM_IP>:8080/docs`

---

## 🔁 Auto-Restart with systemd

Create a systemd unit:

```ini
[Unit]
Description=Iris ML API container
After=docker.service
Requires=docker.service

[Service]
Restart=always
ExecStart=/usr/bin/docker start -a iris-container
ExecStop=/usr/bin/docker stop -t 2 iris-container

[Install]
WantedBy=multi-user.target
```

Enable and reboot:

```bash
sudo systemctl daemon-reexec
sudo systemctl enable iris-api
sudo reboot
```

---

## 🧪 Testing & Logs

### ✅ Sample Test

```bash
curl -X POST http://<YOUR_VM_IP>:8080/predict \
-H "Content-Type: application/json" \
-d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

Expected output:

```json
{"prediction": 0}
```

Logs are saved in `log.txt`.

---

### ✅ Unit Test

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_predict():
    response = client.post("/predict", json={"features": [5.1, 3.5, 1.4, 0.2]})
    assert response.status_code == 200
    assert "prediction" in response.json()
```

Run it:

```bash
pytest test_main.py
```

---

## 📂 File Structure

```
.
├── main.py
├── train.py
├── model.joblib
├── Dockerfile
├── requirements.txt
├── test_main.py
└── README.md
```

---

## 📸 Screenshots to Include

* Swagger UI running
* curl output from terminal
* GCP VM dashboard (show IP + port)
* Docker container running
* systemd service status

---

## 🧠 Real-World Application

This simulates a **production ML API deployment**, helpful for:

* Learning MLOps
* DevOps + Python portfolio
* Resume-ready cloud project

---

## 👤 Author

Built as a personal MLOps demo project.
🔗 Connect on [LinkedIn](https://www.linkedin.com/786akshatk/)
              [Portfolio](https://akshatkashyap.cloud/)

---

## 🏷️ Tags

`#MLOps #FastAPI #Docker #GCP #MachineLearning #Cloud #DevOps #Python #ResumeProject`
