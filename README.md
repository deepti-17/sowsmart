# 🌾 Crop Recommendation System

A machine learning-based crop recommendation system that suggests the most suitable crops to cultivate based on soil and environmental parameters. Built as part of a government-funded internship under the **Crop Residue Management Project** at SLIET, Punjab (Funded by **Anusandhan National Research Foundation (ANRF)**).

---

## 📌 Project Summary

The goal of this project is to assist farmers in making data-driven decisions by analyzing environmental and soil features using a machine learning model trained on real-world agricultural data.

### ✅ Core Functionality:
- Users enter **soil nutrients (N, P, K)**, **pH**, **temperature**, **humidity**, and **rainfall**.
- The model predicts the **optimal crop** to grow under those conditions.
- Deployed as:
  - 🌐 A web application
  - 📱 An Android mobile app

---

## 🚀 Features

- ✅ Input soil and climate data to get crop recommendations
- ✅ Trained using supervised learning algorithms (Random Forest, SVM, etc.)
- ✅ Web interface for farmers and agronomists (Flask based)
- ✅ Android mobile app built using Kotlin
- ✅ Dataset visualization and preprocessing

---

## 🛠️ Tech Stack

| Component             | Tools Used                          |
| --------------------- | ----------------------------------- |
| Machine Learning      | Python, scikit-learn, pandas, NumPy |
| Frontend (Web)        | HTML / CSS                          |
| Backend (Web)         | Flask                               |
| Mobile App            | Android (Kotlin)                    |
| Deployment (Optional) | Firebase / Heroku / Local Server    |

---

## 📊 Machine Learning Models

- Used multiple models and compared accuracies:

| **Model**              | **Accuracy (%)** |
| ---------------------- | ---------------- |
| Naive Bayes            | 99.55            |
| Random Forest          | 99.32            |
| Bagging                | 99.09            |
| Decision Tree          | 98.64            |
| Support Vector Machine | 96.82            |
| Logistic Regression    | 96.36            |
| K-Nearest Neighbors    | 95.91            |
| Gradient Boosting      | 98.18            |
| Extra Trees            | 88.64            |
| AdaBoost               | 14.55            |

Finally used Random Forest and Gaussian Naive Bayes to predict the results.

