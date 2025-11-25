Project Statement – Alzheimer’s Detection Using Longitudinal Data

1. Problem Statement

Traditional Alzheimer’s detection relies on static, single-time clinical assessments. However, Alzheimer’s is a progressive condition, and early markers appear slowly over time.

The challenge: Can a machine learning model detect Alzheimer’s earlier by analyzing multiple visits for each patient.


This project aims to build a longitudinal time-series model that detects cognitive decline patterns more accurately than cross-sectional models.


2. Scope of the Project

The scope includes:

1)Working with a longitudinal dataset containing repeated measures (MMSE, CDR, biomarkers, etc.)

2)Preprocessing, normalization, and temporal structuring

3)Designing and training ML/DL models

4)Evaluating classification performance

5)Visualizing disease progression patterns


Not included:

-MRI image processing

-Real clinical deployment

-Medical diagnosis for real patients


3. Target Users

-Medical researchers

-Machine learning students

-Healthcare data scientists

-Neurology domain learners

-Students doing AI in healthcare projects


4. High-Level Features

-Data Preprocessing-Handles missing values, normalization, temporal ordering.

-Time-Series Feature Extraction-Groups visits per patient to create longitudinal sequences.

- ML/DL Model Training

-Supports:

-LSTM

-Random Forest


5. Performance Evaluation

-Accuracy, confusion matrix.

-Visualization

-Training plots and feature trends.


6. Modular Architecture

-Each part—preprocessing, training, evaluation—is separate for clarityand debugging.



