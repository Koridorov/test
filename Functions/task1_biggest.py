def biggest_number(a:list):
    """Finds the biggest out of three numbers in a list"""
    if a.count>3:
        return "Too many numbers entered."
    for item in a:
        if item>=a[0] and item>=a[1] and item>=a[2]:
            return item

def input_number():
    """Makes user input an int var"""
    num=int(input("Enter a number: "))
    return num

templist=list()

for i in range(3):
    templist.append(input_number())

print(biggest_number(templist))
