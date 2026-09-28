def sum_list(lst:list, sum_total):
    """Finds the sum of the ints in the list. """
    if len(lst)==0:
        return sum_total
    sum_total+=lst[(len(lst)-1)]
    lst.pop()
    return sum_list(lst, sum_total)

lst=[1,2,3,4,5,6,7,8,9,10,11]

print(sum_list(lst,0))