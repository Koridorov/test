#Prompt the user to enter the total driving distance.

#Prompt the user to enter their vehicle's fuel efficiency (e.g., miles per gallon or kilometers per unit).

#Prompt the user to enter the current price of fuel per unit.

#Prompt the user to enter the number of people splitting the cost.

#Calculate the total fuel required, the total cost of the trip, and how much each person owes.

#Print the results clearly using f-strings and proper currency formatting.

import math

distance=float(input("Enter your total driving distance (in km): "))
fuel_efficiency=float(input("Enter your vehicle's fuel efficiency (L/100km): "))
fuel_price=float(input("Enter the fuel price per L (in $): "))
people=float(input("Enter the number of people splitting the cost: "))

#calculations

fuel_amount=float(distance*(fuel_efficiency/100))
#this is the amount of fuel required for the journey. By dividing we get efficency/km
total=float(round(fuel_amount*fuel_price, 2))
#this is the total price
individual=float(((math.ceil(total*100))/people)/100)
#this is the price for each participant
individual_rounded=float(math.ceil(individual*100)/100)
#this is me rounding it up in case the calculation is not perfect
leftovers=float((individual_rounded*people)-total)
#these are the leftovers, should the calculation not be perfect

#prints
print(f"For this trip you require {fuel_amount:.2f} litres of fuel.")
print(f"The total cost of this trip is ${total:.2f}.")
print(f"Each person owes ${individual_rounded:.2f}.")

if (leftovers>0): 
    if(leftovers<1):
        print(f"There will be {int(leftovers*100)} cents left over.")
    else:
        print(f"There will be ${leftovers:.2f} left over.")
else:
    print("There will be no leftover money.")