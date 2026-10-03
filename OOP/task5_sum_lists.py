from functools import reduce

def sum_lists(lst:list) -> int:
    """This returns the sum of all ints in a series of inserted lists"""
    final_list=[]
    if len(lst)==0:
        return []
    if isinstance(lst[0], list):
        return sum_lists(lst[0]) + sum_lists(lst[1:])
    else:
        return [lst[0]] + sum_lists(lst[1:])
print(reduce(lambda x,y: x+y, sum_lists([1,2,[3,4],[[5],6]])))

def merge_lists(lst:list) -> int:
    """This returns the sum of all ints in a series of inserted lists"""
    final_list=[]
    if isinstance(lst[0], list):
        return merge_lists(lst[0]) + merge_lists(lst[1:])
    if len(lst)==1:
        return [lst[0]]
    else:
        return [lst[0]] + merge_lists(lst[1:])