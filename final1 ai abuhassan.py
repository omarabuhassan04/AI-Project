print("Hi! I’m your assistant. Let’s assess the risk of heart disease.\n")


age = float(input("Enter age (in years): "))
trestbps = float(input("Enter resting blood pressure (in mm Hg): "))
chol = float(input("Enter cholesterol level (in mg/dL): "))
thalach = float(input("Enter maximum heart rate achieved: "))

if age > 65 and chol > 240 and trestbps > 160 and thalach < 90:
    print("\nThe patient is at very high risk of heart disease due to advanced age, critical cholesterol levels, very high blood pressure, and low heart rate.")
elif age > 60 and chol > 220 and trestbps > 140 and thalach < 100:
    print("\nThe patient is at high risk of heart disease due to advanced age, high cholesterol, elevated blood pressure, and reduced heart rate.")
elif age > 50 and chol > 200 and trestbps > 130 and thalach < 110:
    print("\nThe patient is at moderate risk of heart disease due to age, mildly elevated cholesterol, and slightly high blood pressure.")
elif age > 40 and chol > 180 and trestbps <= 130:
    print("\nThe patient is at low risk of heart disease but should monitor cholesterol levels.")
elif chol > 250:
    print("\nThe patient has a cholesterol-related risk of heart disease. Consider dietary changes and consulting a doctor.")
elif trestbps > 150:
    print("\nThe patient has a blood pressure-related risk of heart disease. Consider lifestyle changes to lower blood pressure.")
elif thalach < 90:
    print("\nThe patient has a heart rate-related risk of heart disease. Consult a cardiologist.")
else:
    print("\nThe patient has a lower risk of heart disease based on the provided data.")


print("\nRemember, this is a basic estimation. Please consult a doctor for a professional diagnosis.")