# 📰 AI Fake News Detector

An AI-based web application that detects whether a given news article is **Real** or **Fake** using **Natural Language Processing (NLP)** and **Machine Learning** techniques.  
This project aims to reduce the spread of misinformation and promote trustworthy information, aligning with **UN SDG 16 – Peace, Justice & Strong Institutions**.

---

## 🎯 Problem Statement
The rapid spread of fake news on digital platforms has become a major social issue, influencing public opinion and creating misinformation. Manual verification of news is time-consuming and unreliable at scale. This project addresses the problem by providing an automated AI-based system that classifies news articles as real or fake based on textual analysis.

---

## 💡 Solution Overview
The system uses NLP techniques to preprocess news text and extract meaningful features using TF-IDF vectorization. A supervised machine learning model (Logistic Regression) is trained on labeled news data to classify articles. The trained model is deployed using a Flask backend and accessed through a user-friendly web interface.

---

## 🛠️ Technologies Used

### Core Technologies
- Python  
- Natural Language Processing (NLP)  
- TF-IDF Vectorization  
- Machine Learning (Logistic Regression)  
- Flask (Backend API)  
- HTML, CSS, JavaScript (Frontend)  
- Pickle (Model Serialization)

### Future Enhancements
- Retrieval-Augmented Generation (RAG)  
- Agentic AI  
- Large Language Models (IBM Granite – Conceptual)

---

## 👥 Target Users
- General internet users  
- Students and researchers  
- Journalists and content creators  
- Educational institutions promoting media literacy  

---

## 🌍 SDG Alignment
**SDG 16 – Peace, Justice & Strong Institutions**

The project helps combat misinformation, supports access to reliable information, and encourages responsible news consumption.

---

## ⚙️ Project Architecture
1. User inputs a news article via the web interface  
2. Text is sent to the Flask backend  
3. NLP preprocessing and TF-IDF vectorization are applied  
4. Machine learning model predicts Real or Fake  
5. Result is displayed on the UI  

---

