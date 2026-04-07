# ❤️ Heart Disease Risk Prediction — AI Project
## 📌 Project Overview  

This project uses **Artificial Intelligence (Machine Learning)** to predict whether a patient is at risk of heart disease based on their medical data.
## 🎯 Features 

- ✅ Predicts heart disease risk using **K-Nearest Neighbors (KNN)** algorithm
- ✅ Takes patient medical data as input (age, blood pressure, cholesterol, etc.)
- ✅ Outputs a clear prediction: **At risk** or **Not at risk**
- ✅ Displays model accuracy, classification report, and confusion matrix
- ✅ Includes a simple rule-based assistant version for quick estimations

---
## 🧠 How It Works 

1. **Load Dataset** — Reads a CSV file containing disease symptoms and patient profiles
2. **Preprocess Data** — Handles missing values and scales features using `StandardScaler`
3. **Train Model** — Trains a **KNN Classifier** (k=5) on 80% of the data
4. **Evaluate** — Tests on the remaining 20% and prints accuracy + detailed report
5. **Predict** — Takes new patient input and predicts heart disease risk


## 🛠️ Technologies Used 

- **Python 3**
- **pandas** — Data loading and manipulation
- **scikit-learn** — ML model (KNN), preprocessing, evaluation
- **StandardScaler** — Feature normalization
- **KNeighborsClassifier** — Classification algorithm
---
## 📊 Dataset 

- **Name:** Disease Symptom and Patient Profile Dataset
- **Source:** CSV file — `Disease_symptom_and_patient_profile_dataset.csv`
- **Target Column:** `Outcome Variable` (1 = At risk, 0 = Not at risk)
---
---

## 📝 Disclaimer  

> ⚠️ This tool is for **educational purposes only**. It is **not** a substitute for professional medical advice. Always consult a qualified doctor for diagnosis and treatment.
>
> هذه الأداة لأغراض تعليمية فقط. لا تُغني عن استشارة طبيب متخصص.
