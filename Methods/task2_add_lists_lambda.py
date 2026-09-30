def add_lists(*lst) -> list:
    for i in range(2):
       return list(map(lambda *args: sum(args), *lst))

    

    
    
list1=[1,2,3]
list2=[4,5,6]
list3=[7,8,9]
print(add_lists(list1,list2,list3))