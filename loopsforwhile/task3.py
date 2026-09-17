#Задача 3:
#Да се намери и принтира сумата на всички числа, които се делят на 3 и 5, по-малки от 10000.
total=0
#for i in range(10000):
#    if i%3==0 and i%5==0:
#        total+=i
#print(total)
i=0
while i<=10000:
    if i%3==0 and i%5==0:
        total+=i
    i+=1
print(total)