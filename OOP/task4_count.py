def symbol_count(string:str) -> dict:
    counter=dict()
    for _ in string:
        counter[_]=string.count(_)
    return counter

print(symbol_count("obicham da karam kolelo"))