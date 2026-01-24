> LUNA16
> PROJECT
> PLAN


LUNA16 Project

MAI3004 Reproducing AI research (Projects)

Faculty of Health, Medicine, and Life Sciences

Maastricht University

January 2026

PREPARED BY:
Alisa Ovsiannikova,
Tijn Saes,
Csaba Kelemen,
Nienke Wibbelink

SUPERVISED BY:
Sheng Kuang

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

## 2. Resources

### Hardware:
- Access to the university high-performance computing infrastructure (**GPU**): for convolutional operations in neural networks (foundation model) and efficient batch processing

### Software:
- **Google Colab (Python):** for rapid prototyping and shared development (acceptable GPU support especially before access to university facilities is available)
- **GitHub:** for reproducibility, version control, and transparency of experimental workflows
- **ITK-SNAP:** for imaging data visualization (sanity checks)

### Modeling frameworks:
- An open-source **AIM-Harvard foundation model**
- The **Model Genesis** framework to train and compare multiple models for malignancy risk prediction; keep in mind that it includes some CT scans from the LUNA16 dataset in its pre-training data

https://aim-harvard.github.io/foundation-cancer-image-biomarker/ https://github.com/MrGiovanni/ModelsGenesis 

---

## Data

The **LUNA16 (LUng Nodule Analysis 2016)** dataset is a subset of the **LIDC-IDRI** database, focusing on the detection and classification of lung nodules. It contains CT scans with annotated nodule locations and malignancy ratings provided by expert radiologists, serving as a standard benchmark for lung cancer analysis.

**Dataset website:**  
https://luna16.grand-challenge.org/

### LIDC-IDRI
https://www.cancerimagingarchive.net/collection/lidc-idri/

### Data types and formats
- **CT Volumes (MHD):** Volumetric computed tomography scans of the chest.
- **Nodule Annotations (CSV):** Coordinates (x, y, z) of candidate nodules.
- **Clinical / Label Data:** **Malignancy scores** (typically rated 1–5 in the source LIDC-IDRI data, to be binarized for risk prediction):
  - 1, 2 → low risk  
  - 4, 5 → high risk  
  - 3 → decide  
- **Foundation Model:** Pre-trained weights from the **AIM-Harvard** repository.

---

## Relevant publications

- Pai, Suraj, Dennis Bontempi, Ibrahim Hadzic, Vasco Prudente, Mateo Sokač, Tafadzwa L. Chaunzwa, Simon Bernatz et al.  
  *“Foundation model for cancer imaging biomarkers.”*  
  **Nature Machine Intelligence**, 6(3), 2024: 354–367.  
  https://www.nature.com/articles/s42256-024-00807-9

- https://www.sciencedirect.com/science/article/abs/pii/S1361841520302048
- https://pmc.ncbi.nlm.nih.gov/articles/PMC3041807/ - paper abt completing LIDC-IDRI database

## Risk management and documentation
<img width="1358" height="326" alt="Risk management" src="https://github.com/user-attachments/assets/ad721836-665e-4aae-83e2-5eeca87c43df" />

## 4. Technical Obstacles

- **High memory and computing power requirements:**  
  3D image analysis and deep feature extraction require significant GPU memory, especially during fine-tuning.
  - Perform preliminary data exploration image by image (not everything at the same time)
  - Use patches (not full CT scans)
  - Access UM high-performance computing

---

## 5. Ethical and Legal Considerations

### Bias and Generalizability

- **Demographic:**
  - There is little to no metadata available on patient demographics such as race, age, sex, etc. This lack of transparency limits the assessment of potential demographic biases and restricts the generalizability of the results to the broader population.

- **Selection:**
  - LUNA16 consists of patients already suspected of having lung cancer. While this may be representative of a screening population, it is not representative of the general population.

### Data quality

**Origin:**  
   - The LIDC-IDRI dataset, from which LUNA16 is derived, was released in its complete form in 2011, with CT scans originating from the early 2000s (exact years were not found).  
   - 1018 cases were collected, each including a clinical thoracic CT scan and an associated XML file with annotations. Four experienced thoracic radiologists provided the annotations. Four experienced thoracic radiologists independently reviewed each CT scan in a two-phase process to mark and categorize lesions, capturing variability among readers without forcing a consensus.
   - Data protection: The dataset is distributed in anonymized form through repositories such as The Cancer Imaging Archive (TCIA), with direct personal identifiers removed. While fully anonymized data generally falls outside the scope of GDPR, medical images may still carry a risk of re-identification, particularly if combined with external data sources. To mitigate this risk, data will be stored only on access-restricted storage systems and will not be linked with external datasets.
   - Intended use: The primary use of LIDC-IDRI and LUNA16 is scientific research and AI development.
   - License: The full LIDC-IDRI dataset is licensed under CC BY 3.0 Unported, and the LUNA16 subset under CC BY 4.0 International. This allows for redistribution and machine learning use with appropriate attribution. 

## Project Planning – Milestones

### Week 1 – Setting up

| Milestone per week | Tasks                              | Reporting                                   | Responsible body            | Deadline  |
|--------------------|------------------------------------|---------------------------------------------|-----------------------------|-----------|
| 1.1 | Establish scope of research | Project plan and documentation (Google Doc) | Manager | 09/01/26 |
| 1.2 | Set up coding environments | GitHub | SW developer | 07/01/26 |
| 1.3 | Assign roles | Trello | Manager & Communicator | — |
| 1.4 | Consider ethical and legal implications | Project plan | Manager & Communicator | — |
| 1.5 | Decide on a definition of a sample | Project plan and documentation (Google Doc & GitHub) | Data scientist | — |
| 1.6 | Design project plan | Project plan and documentation (Google Doc) | Manager & Communicator | — |
| 1.7 | First look into data | Project plan and documentation (Google Doc) | Data Scientist | — |

### Week 2 – Data preparation

| Milestone per week | Tasks | Reporting | Responsible body | Deadline |
|--------------------|-------|-----------|------------------|----------|
| 2.1 | Pre-processing data (cleaning, imputing, etc.) | Project plan and documentation (Google Doc & GitHub) | SW developer & Data scientist | — |
| 2.2 | Prevent data leakage | Project plan and documentation (Google Doc & GitHub) | SW developer & Data scientist | — |
| 2.3 | Handle class imbalance | Project plan and documentation (Google Doc & GitHub) | SW developer & Data scientist | — |
| 2.4 | Label cleaning and deciding on division of target (3 → low or high risk, or removed?) | Project plan and documentation (Google Doc & GitHub) | SW developer & Data scientist | — |
| 2.5 | Prepare halfway presentation | Google Slides | Communicator | 16/01/26 |
| 2.6 | Prepare updates for coach and team meetings; check that the team is on track | Trello, WhatsApp, Outlook | Manager | — |
| 2.7 | Visualize data and outcomes | GitHub & Google Slides | Communicator | 16/01/26 |

### Week 3 – Training & testing
| Milestone per week | Tasks | Reporting | Responsible body | Deadline |
|--------------------|-------|-----------|------------------|----------|
| 3.1 | Train models | Project plan and documentation (Google Doc & GitHub) | SW developer & Data scientist | — |
| 3.2 | Evaluate and fine-tune models (feature selection?) | Project plan and documentation (Google Doc & GitHub) | SW developer & Data scientist | — |
| 3.3 | Compare models | Project plan and documentation (Google Doc & GitHub) | SW developer & Data scientist | — |
| 3.4 | Visualize data and outcomes | GitHub & Google Slides | Communicator | — |
| 3.5 | Prepare updates for coach and team meetings; check that the team is on track | Trello, WhatsApp, Outlook | Manager | — |

### Week 4 – Finalization
| Milestone per week | Tasks | Reporting | Responsible body | Deadline |
|--------------------|-------|-----------|------------------|----------|
| 4.1 | Double-check workflow and possible mistakes / data leakage / etc. | GitHub | SW developer & Data scientist | — |
| 4.2 | Prepare updates for coach and team meetings; check that the team is on track | Trello, WhatsApp, Outlook | Manager | — |
| 4.3 | Visualize data and outcomes | GitHub & Google Slides | Communicator | — |
| 4.4 | Prepare final presentation | Google Slides | Communicator | 30/01/26 |



