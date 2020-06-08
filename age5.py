# Entering age 
age=int(input("enter your age>"))

# testing the condition
if(age<0):
    print("invaild age")
elif(age>=0 and age<=1):
    print("infant")
elif(age>1 and age<=18):
    print("Child")
elif(age>18 and age<=60):
    print("Adult")
else:
    print("Sr.citizen")











