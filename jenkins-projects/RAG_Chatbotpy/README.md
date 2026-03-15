# 📄 PDF Chatbot using LangChain & Groq (Llama3)

A simple AI-powered chatbot that answers questions from any PDF document.
Built with LangChain, Groq, FAISS, and Streamlit.
Containerized with Docker and automated using Jenkins CI/CD pipeline.

---

## 🚀 What It Does
- Upload any PDF file
- Ask questions about the content
- Get AI-powered answers instantly

---

## 📂 Project Structure
```
pdf-chatbot/
│── app.py                  # Main Streamlit Application
│── requirements.txt        # Python Dependencies
│── Dockerfile              # Docker Image Definition
│── Jenkinsfile             # Jenkins Pipeline Script
│── README.md               # Project Documentation
```

---

## 🛠️ Tech Stack
- Python 3.11
- Streamlit (UI)
- LangChain (AI framework)
- Groq + Llama3 (LLM - fast & free)
- HuggingFace (Embeddings model)
- FAISS (Vector database)
- Docker (Containerization)
- Jenkins (CI/CD pipeline)

---

## ⚙️ Build, Test and Run Workflow

### 1️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 2️⃣ Run Locally
```
streamlit run app.py
```

### 3️⃣ Open In Browser
```
http://localhost:8501
```

### 4️⃣ Get Free Groq API Key
```
https://console.groq.com
Sign up → API Keys → Create New Key
```

---

## 🐳 Running with Docker

### 1️⃣ Build Docker Image
```
docker build -t pdf-chatbot:latest .
```

### 2️⃣ Run Docker Container
```
docker run -p 8501:8501 pdf-chatbot:latest
```

### 3️⃣ Open In Browser
```
http://localhost:8501
```

---

## 🔄 Jenkins Pipeline

The Jenkinsfile automates the following stages:

1. Clone  - Pulls latest code from GitHub
2. Build  - Installs dependencies
3. Docker Build - Builds Docker image
4. Docker Push  - Pushes image to DockerHub
```groovy
pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/BhushanGit04096/pdf-chatbot'
            }
        }
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build -t bhushan0496/pdf-chatbot:latest .'
            }
        }
        stage('Docker Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'bhushan0496',
                    usernameVariable: 'dockeruser',
                    passwordVariable: 'password'
                )]) {
                    sh '''
                        echo "$password" | docker login -u "$dockeruser" --password-stdin
                        docker push bhushan0496/pdf-chatbot:latest
                    '''
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
```

> **Note:** Configure a Jenkins credential named `bhushan0496` with your DockerHub username and password.

---

## 🛠️ Prerequisites

Before running this project install:
- Python 3.11+
- Docker
- Jenkins
- Groq API Key (free at console.groq.com)

---

## 👨‍💻 Author
Bhushaw | https://github.com/BhushanGit04096

---

## 📜 License
This project is released under the MIT License.
