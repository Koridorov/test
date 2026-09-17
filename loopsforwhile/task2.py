#Напишете програма, която принтира дължината на string въведен от потребителя, без да използвате len().
#(Hint: използвайте цикъл, който итерира по символите на string-а)

string=str(input("Enter your string: "))
symbolcount=0
for symbol in string:
    symbolcount+=1
print(symbolcount)