def three_number_arrays(n):
    list_times_three=[]
    for _ in range(n):
        list_times_three.append(_*3)

    list_fibonacci=[]
    num1=1
    num2=1
    list_fibonacci.append(num1)
    list_fibonacci.append(num2)
    if n==1:
        list_fibonacci.pop()
    elif n==0:
        list_fibonacci.pop()
        list_fibonacci.pop()
    elif n>1:
        for _ in range(n-2):
            if num1>=num2:
                num2=num1+num2
                list_fibonacci.append(num2)
            elif num1<=num2:
                num1=num1+num2
                list_fibonacci.append(num1)

    list_multiplicci=[]
    num1=2
    num2=3
    list_multiplicci.append(num1)
    list_multiplicci.append(num2)
    if n==1:
        list_multiplicci.pop()
    elif n==0:
        list_multiplicci.pop()
        list_multiplicci.pop()
    elif n>1:
        for _ in range(n-2):
            if num1>num2:
                num2=num1*num2
                list_multiplicci.append(num2)
            elif num1<num2:
                num1=num1*num2
                list_multiplicci.append(num1)

    print(list_multiplicci, list_fibonacci, list_times_three)

    list_final=[]
    for x,y,z in zip(list_times_three, list_fibonacci, list_multiplicci):
        j=x+y+z
        list_final.append(j)

    print(list_final, list_multiplicci, list_fibonacci, list_times_three)


three_number_arrays(7)