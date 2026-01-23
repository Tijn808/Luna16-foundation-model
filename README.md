> LUNA16
> PROJECT
> PLAN


LUNA16 Project

MAI3004 Reproducing AI research (Projects)

Faculty of Health, Medicine, and Life Sciences

Maastricht University

January 2026

PREPARED BY:
Alisa Ovsiannikova i6365923,
Tijn Saes i6344387,
Csaba Kelemen i6305543,
Nienke Wibbelink i6358957

SUPERVISED BY:
Dr. Sheng Kuang,
Dr. Zohaib Salahuddin

-----------------------------------------------------------------------------------------------------------------

**introduction** 

# 1. Project Overview (from Project Descriptions)

**Title:**  
Foundation Models for Lung Nodule Malignancy Risk Prediction using LUNA16 Dataset

## Goals:

1. **A working and fully reproducible project codebase (Python pipeline: PyTorch) containing:**
   - a. data preparation  
   - b. label creation  
   - c. training (3 models)  
   - d. evaluation  
   - e. comparison  
   - f. ensemble  

2. **A concise results summary including:**
   - a. tables/plots of metrics for each method and diffusion scale (if applicable)  
   - b. statistical or confidence estimates where possible  

3. **A short discussion addressing:**
   - a. what worked  
   - b. what didn’t  
   - c. why (including pitfalls such as imbalance, leakage, label uncertainty)  

## Description / Scope:

Lung cancer screening requires accurate identification and risk stratification of pulmonary nodules. nodules to reduce false positives and improve early detection. Recent advancements in Deep Learning have introduced "Foundation Models" – large-scale, pre-trained networks that capture robust feature representations across diverse medical imaging tasks.
In this project, a malignancy risk prediction workflow will be implemented using an open-source foundation model developed by the AIM-Harvard lab. Instead of handcrafted radiomics, deep learning features will be leveraged to analyze lung nodules from the LUNA16 dataset.
The project involves comparing 3 distinct modeling strategies for malignancy risk prediction: 

1. Logistic Regression using the foundation model features,
2. Multi-Layer Perceptron (MLP) using the foundation model features,
3. Fine-tune the Foundation Model.

## Research Questions:

1. How can an open-source medical imaging foundation model developed by the AIM-Harvard lab be adapted to reliably predict human lung nodule malignancy risk in the **LUNA16 dataset**?
   - a. How well does a logistic regression classifier perform when using deep features extracted from the AIM-Harvard foundation model for lung nodule malignancy prediction?
   - b. Does replacing logistic regression with a multi-layer perceptron (MLP) improve malignancy prediction performance when using foundation model features?
   - c. Does fine-tuning the foundation model outperform fixed-feature approaches (logistic regression and MLP) for lung nodule malignancy prediction?
   - d. How do the three foundation-model–based approaches compare to a Model Genesis–based logistic regression baseline?

