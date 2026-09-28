def dividers(num:int):
    j=0
    for i in str(num):
        if int(i)==0:
            continue
        if num%int(i)==0:
            j+=1
    return j

print(dividers(10))