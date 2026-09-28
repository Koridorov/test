def string_operations(s:str, t:str, k:int) -> str:
    """This checks if string "s" can be made into string "t" with "k" number of .pop or .append"""
    liststart=list(s)
    listfinal=list(t)
    while True:
        for symbol in s:
            if symbol not in listfinal or liststart.index(symbol)!=listfinal.index(symbol):
                k-=1
                liststart.pop()
            
        for symbol in t:
            if symbol not in liststart:
                liststart.append(symbol)
                k-=1

        if liststart==listfinal:
            break
    if k<0:
        return "No"
    return "Yes"
print(string_operations("abc", "def", 6))