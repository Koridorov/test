def string_inverter(strng:str):
    templist=[]
    for symbol in strng:
        templist.append(symbol)
    templist.reverse()

    return "".join(templist)

strng=str(input("Please enter your string: "))

print(string_inverter(strng))