# taking distance travelled
distance_travelled=float(input("Enter the distance travelled>"))

# taking cost of fuel
cost_of_fuel=float(input("Enter the cost of fuel>"))

# taking the car average
car_average=float(input("Enter the car's fuel tank average>"))

# calculating the fuel consumed
fuel_consumed=distance_travelled /car_average

# calculating the cost per day
cost_per_day= fuel_consumed*cost_of_fuel


# rounding the cost per day
cost_per_day = round(cost_per_day,2)

# printing cost per day
print("cost travelling per day is",cost_per_day,"inr" )

