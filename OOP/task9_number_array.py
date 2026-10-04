#An = A(n-1) * A(n-3) - A(n-2) * A(n-4)

def number_array_4(num:int) -> list:
    list_result=[1,2,4,8]
    if num<=4:
        return list_result[:num]
    else: 
        for i in range(4, num):
            j=list_result[i-1]*list_result[i-3]-list_result[i-2]*list_result[i-4]
            list_result.append(j)
        return list_result

print(number_array_4(20))


def get_number_array_element(num:int) -> int:
    if num==1:
        return 1
    elif num==2:
        return 2
    elif num==3:
        return 4
    elif num==4:
        return 8
    else:
        return get_number_array_element(num-1)*get_number_array_element(num-3)-get_number_array_element(num-2)*get_number_array_element(num-4)

def number_array_list(num:int) -> list:
    list_result=[]
    for i in range(1,num+1):
        list_result.append(get_number_array_element(i))
    return list_result

print(number_array_list(20))