# COGNITIME
Early detection of Alzheimer's from patient data early detection and analysis
# Alzheimer’s Detection Using Longitudinal Data

 
1)Project Overview
Alzheimer’s Disease is a progressive neurological disorder. Early detection is often difficult because clinical symptoms develop slowly. This project uses *longitudinal data (multiple patient visits over time) to detect patterns of cognitive decline and classify subjects into:
- Cognitively Normal (CN)
- Mild Cognitive Impairment (MCI)
- Alzheimer’s Disease (AD)

The model learns progression trends, not just one-time measurements, making the predictions more realistic and medically meaningful.

2)Features

- Load and process longitudinal CSV datasets  
- Clean and normalize biomarkers, cognitive scores, and demographic information  
- Group patient data by subject ID and sort by visit time  
- Extract time-series features  
- Train a machine learning/deep learning model (LSTM or classical ML)  
- Predict cognitive state based on multi-visit data  
- Visualize training curves and evaluation metrics  
- Modular, reproducible code structure

 
3) Technologies / Tools Used

- Python 
- NumPy, Pandas – data handling  
- Scikit-learn – preprocessing + classical models  
- TensorFlow– LSTM model  
- Matplotlib – graphs  
- Google Colab* – execution environment


4) Steps to Install & Run the Project

1. Clone the repository*
```bash
git clone <your-repo-link>
cd alzheimers-longitudinal

2. install dependencies
pip install-r requirements.txt

3.Place your data files
/data/

4.Run preprocessing
python src/preprocess.py

5.train the model
python src/train_model.py

6. generate predictions/plots
python src/evaluate.py
```

5)Instructions for testing

1.check if csv loads correctly
2.prepprocess data and ensure no missing values remain
3.run training and observe:
-accuracy
-validation loss
-confusion matrix
4. compare predictrions on
-a real patient sequence
-a modified sequence

6)screenshots
<img width="833" height="705" alt="Screenshot 2025-11-24 155059" src="https://github.com/user-attachments/assets/4ff30445-7fe0-4015-969c-db7eef8fd463" />
<img width="532" height="654" alt="Screenshot 2025-11-24 155126" src="https://github.com/user-attachments/assets/2dc3de9a-233e-4c84-a5e5-dc87be99d6e8" />





