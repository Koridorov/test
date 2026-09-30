def flatten(lst:list) -> list:
    """Puts variables in nested lists into a single list."""
    if len(lst)==0:
        return []
    if type(lst[0])==list:
        return flatten(lst[0]) + (flatten(lst[1:]))
    else:
        return [lst[0]]+flatten(lst[1:])
    


lst=[1,[2],[[3],4],[5,[6,[7,[8]]], [9], [10], [[[[[[[[[[11]]]]]]]]]]]]

print(flatten(lst))