# inputing weight in kg
weight=float(input("Enter your weight in kg>"))

# inputing height in meters
height=float(input("Enter your height in meters =>"))

# calculating bmi
bmi=(weight/height)/height

# rounding bmi
bmi=round(bmi,2)

# printing Bmi
print(bmi)
