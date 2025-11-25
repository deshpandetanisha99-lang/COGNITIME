from google.colab import drive
drive.mount('/content/drive')
# EXCEL READER
!pip install openpyxl xlrd --quiet

#UPLOADING FILE
base_path="/content/drive/MyDrive/brainio/brainio"
from google.colab import files
uploaded = files.upload()

file = list(uploaded.keys())[0]
print("Uploaded file:", file)
#CSV OR EXCEL
import pandas as pd
try:
    #IF CSV
    df = pd.read_csv(file)
    print("Loaded as CSV")
except:
    try:
        #IF EXCEL
        df = pd.read_excel(file, engine='openpyxl')
        print("Loaded as Excel (openpyxl)")
    except:
        try:
            df = pd.read_excel(file, engine='xlrd')
            print("Loaded as Excel (xlrd)")
        except Exception as e:
            print("Could not load file. Error:", e)
            df = None
if df is not None:
    print("\nData Preview:")
    print(df.head())
    print("\nData Info:")
    print(df.info())

#PROCESS
label_col = "Group"
if label_col not in df.columns:
    raise ValueError(f"Label column '{label_col}' not found. Check column names.")

df = df.dropna(subset=[label_col])

X = df.drop(columns=[label_col])
y = df[label_col]

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

X = pd.get_dummies(X)

#NUMERICAL FEATURES SCALING
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#TAIN/TEST
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

#TRAINING
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)
print("\nModel trained successfully!")

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
y_pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

#PREDICTION FOR NEW PATIENT
def predict_patient(values_dict):
    """
    values_dict example: {"Age": 75, "MMSE": 24, "CDR": 1.0, "EDUC": 12}
    """
    temp = pd.DataFrame([values_dict])
    temp = pd.get_dummies(temp)
    temp = temp.reindex(columns=X.columns, fill_value=0)
    temp_scaled = scaler.transform(temp)
    pred = model.predict(temp_scaled)
    return le.inverse_transform(pred)[0]
