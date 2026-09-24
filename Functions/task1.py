#n, m
# n* n+1 *n+2 *n+3...m 
def mutiply(i,j):
    total=1
    for number in range (i,j+1):
        total*=number
    print(total)
#ako iskam da polzvam promenliva izvyn fn ???
i=int(input("Enter the lower range: "))
j=int(input("Enter the higher range: "))
mutiply(i,j)