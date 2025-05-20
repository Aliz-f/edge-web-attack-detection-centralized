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
---

## 📊 Evaluation Metrics

- Accuracy
- Macro and Weighted Precision
- Macro and Weighted Recall
- Macro and Weighted F1-Score
- Confusion Matrix
- Model Size (in MB)
- Inference Time (per sample, in seconds)

---

### 📊 Model Performance Summary

| Task            | Model     | Accuracy | Precision (Macro / Weighted) | Recall (Macro / Weighted) | F1-Score (Macro / Weighted) | AUC (Macro / Weighted) | Inference Time (per sample) |
|-----------------|-----------|----------|-------------------------------|----------------------------|------------------------------|--------------------------|-------------------------------|
| **Binary**      | CNN       | 1.0000   | 1.0000 / 1.0000               | 1.0000 / 1.0000            | 1.0000 / 1.0000              | 1.0000 / 1.0000          | 0.040846 s                   |
|                 | LightGBM  | 1.0000   | 1.0000 / 1.0000               | 1.0000 / 1.0000            | 1.0000 / 1.0000              | 1.0000 / 1.0000          | **0.001268 s**               |
| **6-Class**     | CNN       | 0.9749   | 0.9388 / 0.9796               | 0.9125 / 0.9749            | 0.9150 / 0.9743              | 0.9976 / 0.9993          | 0.028850 s                   |
|                 | LightGBM  | **0.9756** | **0.9815 / 0.9764**         | **0.9792 / 0.9756**        | **0.9800 / 0.9756**          | **0.9993 / 0.9991**      | **0.000917 s**               |
| **15-Class**    | CNN       | **0.9701** | 0.8896 / **0.9726**         | **0.8904 / 0.9701**        | **0.8871 / 0.9707**          | **0.9984 / 0.9995**      | 0.049419 s                   |
|                 | LightGBM  | 0.9645   | **0.9631 / 0.9651**           | 0.9608 / 0.9645            | 0.9617 / 0.9646              | 0.9993 / 0.9993          | **0.001006 s**               |

---

## ⚙️ Experimental Settings

- All models are tested under both:
  - **IID Settings** — Equal data distribution across clients
  - **Non-IID Settings** — Skewed or imbalanced data across clients (simulating real-world edge environments)
- Future work includes:
  - Full integration with the **Flower framework** for federated learning
  - Comparison of centralized vs. federated performance

---