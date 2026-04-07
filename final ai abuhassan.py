
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler


data=pd.read_csv("/content/Disease_symptom_and_patient_profile_dataset.csv")


if data.isnull().sum().any():
    data.fillna(data.median(), inplace=True)


X = data.drop("Outcome Variable", axis=1)  
y = data["Outcome Variable"]  


scaler = StandardScaler()
X = scaler.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


knn = KNeighborsClassifier(n_neighbors=5)  
knn.fit(X_train, y_train)


y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


print("\nEnter the new patient's data:")
new_patient = [
    float(input("Age: ")),
    float(input("Resting Blood Pressure: ")),
    float(input("Cholesterol Level: ")),
    float(input("Maximum Heart Rate Achieved: ")),
    int(input("Fasting Blood Sugar (1 for True, 0 for False): ")),
    int(input("Chest Pain Type (0, 1, 2, or 3): ")),
    int(input("Resting ECG (0, 1, or 2): ")),
    float(input("Oldpeak (ST Depression Induced by Exercise): ")),
    int(input("Slope of Peak Exercise ST Segment (0, 1, or 2): ")),
    int(input("Number of Major Vessels Colored by Fluoroscopy (0-3): ")),
    int(input("Thalassemia (1 for Normal, 2 for Fixed Defect, 3 for Reversible Defect): "))
]


new_patient_info = scaler.transform([new_patient])
prediction = knn.predict(new_patient_info)


if prediction[0] == 1:
    print("\nPrediction: The patient is at risk of heart disease.")
else:
    print("\nPrediction: The patient is not at risk of heart disease.")




