for i in range(0,4):
    for k in range (4,i,-1):
        print(" ", end="")
    for j in range (1,(i+1)*2):
        print("*", end="")
    print()
for i in range(4,-1,-1):
    for k in range(4,i,-1):
        print(" ",end="")
    for j in range (1,(i+1)*2):
        print("*", end="")
    print()