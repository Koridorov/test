#При вход от потребителя цяло число, изпълнете следните условни действия:

#а) Ако числото е нечетно - да се принтира “Losho”;
#б) Ако числото е четно и е между 2 и 5 - да се принтира “Dobre”;
#в) Ако числото е четно и е между 6 и 20 - да се принтира “Losho”;
#г) Ако числото е четно и е по-голямо от 20 - да се принтира “Dobre”.

chislo=int(input("Enter your number: "))
if (chislo%2!=0):
    print("Losho")
elif (chislo%2==0 and chislo>2 and chislo<5):
    print("Dobre")
elif (chislo%2==0 and chislo>6 and chislo<20):
    print("Losho")      
elif (chislo%2==0 and chislo>20):
    print("Dobre")