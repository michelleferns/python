# Entering weight 
weight=float(input("Enter your weight in kg >"))

# Entering height
height=float(input("Enter your height in meters >"))

#calculating bmi
bmi=(weight/height)/height

# Rounding off
bmi=round(bmi,2)

# testing the condition
if(bmi>=0 and bmi< 18.5):
  print("You are under weight")
elif(bmi>=18.5 and bmi<24.9):
  print("You are normal weight")
elif(bmi>=25 and bmi<29.9):
  print("You are over weight")
else:
  print("You are in obesity")
  
# Printing  bmi
print("My bmi is",bmi)
 
