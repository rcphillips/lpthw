#assigns numbers to variables
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
#performs calculations using these assigned values to generate a new assigned value
cars_not_driven = cars - drivers
#makes a new variable with the exact same value as an old variable
cars_driven = drivers
#as above, performs calculations using existing variables
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

#Study Drills:
#The issue is that he used two incorrectly named variables. So when
#the code gets to line 8, it's asked to name a variable based on other variables that it
#doesn't have. Result: a "NameError" on line 8, specifically, the first variable that is incorrectly named,
#and so, 'missing': car_pool_capacity.
#the calculation is also bizarre, but that's not why there's an error.

#1. Nothing bad happens. But the float class doesn't propogate to future calculations,
#	as it does in the actual code used.
#2. I will remember that you have to use 4.0 to make it a floating point number.
#3. Commenting.
#4. I am sure that = is called equals. And some say it's ASSIGNING values to variables.
#5.	I remember that _ is called an underscore.
#6. I did it.