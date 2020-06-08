# inputing your height in feet part
foot=int(input("enter your height in foot>"))

# inputing your height in inch part
inch=int(input("enter your height in inch>"))

# converting feet to meter
feet_to_meter=foot*0.3048

# converting inch to meter
inch_to_meter=inch*0.0254

# adding feet to meter
total_height=feet_to_meter+inch_to_meter

# converting meters to cm
total_height_in_cm=total_height*100

# printing the height
print("My height is",total_height,"meters")


# printing the height
print("My height is",total_height_in_cm,"centimeters")
