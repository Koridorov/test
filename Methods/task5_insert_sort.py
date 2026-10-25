def insert_sorted(lst:list, item:str|int) -> list:
    for i in range(len(lst)):
        if i==0 and item<=lst[i]:
            lst.insert(i,item)
            return lst
        elif i==(len(lst)-1) and item>=lst[i]:
                lst.append(item)
                return lst
        elif lst[i]<=item<=lst[i+1]:
            lst.insert(i+1, item)
            return lst
        
def insert_sorted_sort(lst:list, item:str|int) -> list:
     lst.append(item)
     lst.sort()
     return lst
print(insert_sorted_sort([2,4], 1))