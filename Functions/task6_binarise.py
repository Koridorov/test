def binarise(number:int):
    if number not in range(0,1001):
        return "Please input a valid number."

    i=number
    binary=[]
    while True:
        j=str(i%2)
        i=i//2
        binary.append(j)
        if i==0:
            break
        else:
            continue
    binary.reverse()
    return "".join(binary)

#n=int(input("Please enter a number between 1-1000: "))
#print(binarise(n))
k=0
num=0
while k<20:
    num+=1
    if binarise(num).count("1")==binarise(num).count("0"):
        print(num, binarise(num))
        k+=1
        