a=float(input("Enter first side of triangle >"))
b=float(input("Enter second side of triangle >"))
c=float(input("Enter third side of triangle >"))
s = (a+b+c)/2
import math
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area of triangle is", area)
