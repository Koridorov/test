def indexirane(lst:list, string:str):
    if string in lst:
        return lst.index(string)
    else:
        return -1

templist=["a", "b", "c", "d", "myEl", "e", "123"]
string=input("Enter your string: ")

print(indexirane(templist, string))