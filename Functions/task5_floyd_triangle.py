rows=int(input("Enter the number of rows: "))
def floyd_triangle(rows):
    num=1
    for i in range(1,rows+1):
        for j in range(0,i):
            print(num, end=" ")
            num+=1
        print()    

        
floyd_triangle(rows)