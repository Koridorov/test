from math import ceil

#inputs:
bill=float(input("What is the total bill amount?"))
#Maybe this needs to be float?
tip=float(input("What percentage tip do you want to leave?"))
people=int(input("How many people are splitting the bill?"))

#calculations:
raw_tip=float(tip*bill/100)
#I dont know how to do %ages, so this is the formula
tip_amount=float(round(raw_tip*100)/100)
total=float(tip_amount+bill)
#If bill is float, this needs to be float too
individual=float(total/people)
individual_rounded=float(ceil(individual*100)/100)
leftovers=float(ceil(((individual_rounded*people)-total)*100)/100)
#Is there a way to make the .0 disappear if the result is a whole number?

#prints
print(f"Tip amount is ${tip_amount:.2f}.")
print(f"Grand total is ${total:.2f}.")
print(f"Each person owes ${individual_rounded:.2f}.")
print(f"There will be ${leftovers:.2f} left over.")
#ai corrections:
#every amount has to be float. Before that some of them were coded as "int", and because of that calculations were incorrect. 
#":.2f" - no idea how im supposed to come up with that. 
# Apparently no easier way to do %. 
# the entire math and ceil - no idea this existed.

#my own corrections
#ceil the tip amount
#then I thought round instead of ceil, since the tip amount matters less and ceil produced unwanted results
#the entire leftovers section. also ceiled. 