#Напишете програма, която принтира таблицата за умножение от 1 до 10
#1 2 3 4 5 6 7 8 9 10
for i in range(1,11):
    for j in range(1,11):
        if i*j<10:
            print(str(i*j) + " ", end=" ")
        else:
            print(i*j, end=" ")
    print()