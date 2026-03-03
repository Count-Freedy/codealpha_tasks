# CodeAlpha AI/ML Internship Projects

This repository contains the projects completed during my **AI/ML Internship at CodeAlpha**. These tasks demonstrate proficiency in Natural Language Processing (NLP), API integration, and Computer Vision.

---

## 🛠️ Technology Stack
* **Language:** Python 3.10+
* **Framework:** Streamlit (Web UI)
* **AI/ML Libraries:** Ultralytics (YOLO11), Sentence-Transformers, Deep-Translator
* **Utilities:** OpenCV, gTTS (Google Text-to-Speech), Scikit-learn

---

## 📁 Project Details

### 1. AI Multi-Language Translation Tool
A professional translation tool that allows users to translate text across 50+ languages with built-in easy Copy-to-Clipboard support.
* **Key Features:** Auto-language detection and Copy-to-Clipboard functionality.
* **Implementation:** Integrated `deep-translator` API for high-accuracy translation and `gTTS` for voice synthesis.

### 2. Smart Chatbot for FAQs
An intelligent assistant designed to handle user queries using Semantic Search.
* **Key Features:** 50+ FAQ entries, sidebar quick-access buttons, and confidence score display.
* **Implementation:** Uses the `all-MiniLM-L6-v2` Transformer model to calculate **Cosine Similarity** between user intent and the knowledge base.

### 3. Real-Time Object Detection & Tracking
A high-performance Computer Vision system for identifying and tracking objects in real-time.
* **Key Features:** Unique ID assignment for each object, persistence tracking (ByteTrack), and a live object counter.
* **Implementation:** Built using the state-of-the-art **YOLO11** architecture and OpenCV for real-time video stream processing.

---

## 🚀 Installation & Usage

1. Clone the repository
   ```bash
   git clone https://github.com/Count-Freedy/codealpha_tasks.git
   cd CodeAlpha_Internship

2. Create and Activate Virtual Environment
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1 

3. Install All Dependencies
   ```bash
   pip install streamlit ultralytics deep-translator gTTS sentence-transformers scikit-learn opencv-python-headless st-copy-to-clipboard

# --- HOW TO RUN THE TASKS ---

1. To run Task 1: AI Multi-Language Translation Tool
   ```bash
    streamlit run Task1/app.py

2. To run Task 2: Smart Chatbot for FAQs
   ```bash
    streamlit run Task2/app.py

3. To run Task 3: Real-Time Object Detection & Tracking
   ```bash
    streamlit run Task3/app.py
   
---

## 📊 Project Outputs

<img width="1365" height="629" alt="AI-translator" src="https://github.com/user-attachments/assets/48c82030-c156-4cf2-9e29-19900a44bb56" />
<img width="1365" height="628" alt="Chatbot-for-FAQs" src="https://github.com/user-attachments/assets/19f5becd-8b44-4663-8a65-b2b9b7eae34b" />
<img width="1364" height="627" alt="Object-Detection" src="https://github.com/user-attachments/assets/a9ac44f8-5a94-45f3-b8b1-c616834394e8" />

---

Author: Kunal Kumar Chauhan

