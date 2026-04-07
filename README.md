# ❤️ Heart Disease Risk Prediction — AI Project
### مشروع الذكاء الاصطناعي للتنبؤ بخطر أمراض القلب

---

## 📌 Project Overview | نظرة عامة

This project uses **Artificial Intelligence (Machine Learning)** to predict whether a patient is at risk of heart disease based on their medical data.

يستخدم هذا المشروع **الذكاء الاصطناعي (تعلم الآلة)** للتنبؤ بما إذا كان المريض معرضًا لخطر الإصابة بأمراض القلب بناءً على بياناته الطبية.

---

## 🎯 Features | المميزات

- ✅ Predicts heart disease risk using **K-Nearest Neighbors (KNN)** algorithm
- ✅ Takes patient medical data as input (age, blood pressure, cholesterol, etc.)
- ✅ Outputs a clear prediction: **At risk** or **Not at risk**
- ✅ Displays model accuracy, classification report, and confusion matrix
- ✅ Includes a simple rule-based assistant version for quick estimations

---

## 🧠 How It Works | كيف يعمل

1. **Load Dataset** — Reads a CSV file containing disease symptoms and patient profiles
2. **Preprocess Data** — Handles missing values and scales features using `StandardScaler`
3. **Train Model** — Trains a **KNN Classifier** (k=5) on 80% of the data
4. **Evaluate** — Tests on the remaining 20% and prints accuracy + detailed report
5. **Predict** — Takes new patient input and predicts heart disease risk

---

## 🗂️ Project Files | ملفات المشروع

| File | Description |
|------|-------------|
| `final ai abuhassan.py` | Main ML model using KNN + StandardScaler |
| `final1 ai abuhassan.py` | Simple rule-based heart disease assistant |
| `finalcode1.ipynb` | Jupyter Notebook (version 1) |
| `finalcode2.ipynb` | Jupyter Notebook (version 2 - full analysis) |
| `model.pkl` / `model1.pkl` / `model2nd.pkl` | Saved trained models |

---

## 🛠️ Technologies Used | التقنيات المستخدمة

- **Python 3**
- **pandas** — Data loading and manipulation
- **scikit-learn** — ML model (KNN), preprocessing, evaluation
- **StandardScaler** — Feature normalization
- **KNeighborsClassifier** — Classification algorithm

---

## 📊 Dataset | مجموعة البيانات

- **Name:** Disease Symptom and Patient Profile Dataset
- **Source:** CSV file — `Disease_symptom_and_patient_profile_dataset.csv`
- **Target Column:** `Outcome Variable` (1 = At risk, 0 = Not at risk)

---

## ▶️ How to Run | طريقة التشغيل

### 1. Install dependencies
```bash
pip install pandas scikit-learn
```

### 2. Run the main model
```bash
python "final ai abuhassan.py"
```

### 3. Enter patient data when prompted:
```
Age: 55
Resting Blood Pressure: 140
Cholesterol Level: 230
Maximum Heart Rate Achieved: 150
...
```

### 4. Get prediction:
```
Prediction: The patient is at risk of heart disease.
```

---

## 📈 Model Performance

The model is evaluated using:
- **Accuracy Score**
- **Classification Report** (Precision, Recall, F1-Score)
- **Confusion Matrix**

---

## 👤 Author | المؤلف

**Omar Abuhassan**
- 🎓 AI Course Final Project
- 📅 2026

---

## 📝 Disclaimer | إخلاء المسؤولية

> ⚠️ This tool is for **educational purposes only**. It is **not** a substitute for professional medical advice. Always consult a qualified doctor for diagnosis and treatment.
>
> هذه الأداة لأغراض تعليمية فقط. لا تُغني عن استشارة طبيب متخصص.
