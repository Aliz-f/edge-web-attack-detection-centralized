# Web Attack Detection on Edge-IIoTset

This repository contains machine learning and deep learning models for detecting web-based cyberattacks using the Edge-IIoTset dataset. The focus is on designing lightweight, high-performance models optimized for deployment in edge computing environments, where resources are constrained.

We implement and evaluate models across **three classification tasks**:
- **Binary Classification** — Distinguishing between benign and malicious traffic.
- **6-Class Classification** — Categorizing attacks into major threat groups.
- **15-Class Classification** — Fine-grained identification of specific attack types.

---

## 🚀 Project Goals

- Build and benchmark a variety of machine learning and deep learning models, including:
  - LightGBM (tree-based ensemble model)
  - 1D Convolutional Neural Network (1D-CNN)
  - MobileNet-1D (lightweight CNN for edge deployment)
  - Micro-CNN (minimalist CNN for extreme resource constraints)
  - Hybrid CNN+LSTM+GRU architecture (combining spatial and temporal features)
- Support binary, 6-class, and 15-class classification tasks.
- Design models with edge deployment in mind (small memory footprint, fast inference).
- Compare performance on multiple metrics including classification accuracy, generalization, and runtime efficiency.
- Explore both **IID** and **Non-IID** data distributions in the context of federated learning.

---

## 📂 Dataset

**Edge-IIoTset** is a publicly available dataset designed for evaluating security solutions in Industrial IoT (IIoT) environments, particularly under edge computing scenarios.

📎 [Kaggle: Edge-IIoTset Dataset](https://www.kaggle.com/datasets/iotfleet/edgeiiotset)

---

## 🔢 Classification Tasks

| Task                   | Classes                                                                 |
|------------------------|-------------------------------------------------------------------------|
| **Binary**             | `Normal`, `Attack`                                                      |
| **6-Class**            | `Normal`, `DDoS`, `Injection`, `MITM`, `Scanning`, `Malware`            |
| **15-Class**           | Includes all subtypes (e.g., `DDoS-TCP`, `SQL Injection`, etc.)         |

---

## 🛡️ Attack Categories

- **DDoS (Distributed Denial of Service)**
- **Injection Attacks** (e.g., SQL, Command)
- **MITM (Man-in-the-Middle) Attacks**
- **Malware Attacks**
- **Brute Force / Password Attacks**
- **Scanning and Probing Attacks**

---

## 🧠 Models Implemented

| Model                     | Description                                                              |
|---------------------------|--------------------------------------------------------------------------|
| **LightGBM**              | Gradient boosting model optimized for speed and interpretability         |
| **1D-CNN**                | Efficient convolutional architecture for time-series security data       |
| **MobileNet-1D**          | Lightweight convolutional network tailored for edge computing            |
| **Micro-CNN**             | Simplified CNN with minimal parameters, ideal for microcontrollers       |
| **CNN + LSTM + GRU**      | Hybrid model combining spatial (CNN) and sequential (LSTM/GRU) learning |

---

## 📊 Evaluation Metrics

- Accuracy
- Precision, Recall
- Macro and Weighted F1-Score
- Confusion Matrix
- Model Size (in MB)
- Inference Time (per sample, in milliseconds)

---

## ⚙️ Experimental Settings

- All models are tested under both:
  - **IID Settings** — Equal data distribution across clients
  - **Non-IID Settings** — Skewed or imbalanced data across clients (simulating real-world edge environments)
- Future work includes:
  - Full integration with the **Flower framework** for federated learning
  - Comparison of centralized vs. federated performance

---