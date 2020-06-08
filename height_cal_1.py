#  Entering height in foot
foot=float(input("Enter your height in foot"))

#  Entering height in foot
inch=int(input("Enter your height in inch"))

# Converting foot to meters
feet_to_meters=foot*.3048

# Converting inch to meters
inch_to_meters=inch*.0254

# Adding foot & inch
total_height=feet_to_meters + inch_to_meters

# Converting total height to cm
cm=total_height * 100

# printing total_height 
print("My height is",total_height,'meters')

# Printing cm
print('My height is',cm,'cenitimeters')
