def list_operator(list:list, operator, num:int):
    listtemp=[]
    for i in list:
        if operator=="+":
            listtemp.append(i+num)
            
        elif operator=="*":
            
            listtemp.append(i*num)

        elif operator=="-":
            
            listtemp.append(i-num)

        elif operator=="/":
            
            listtemp.append(i/num)

    return listtemp

testlist=[5,5,1,6]
operator=input("Enter your operator: ")
num=int(input("Enter the number: "))


print(list_operator(testlist, operator, num))