def sum_list(lst: list) -> int:
    """Finds the sum of the ints in the list."""
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])
lst=[1,2,3,4,5,6,7,8,9,10,11]

print(sum_list(lst,0))