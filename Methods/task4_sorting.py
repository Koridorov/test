def sorted_list(lst:list) -> list:
    """This checks if the list of integers is sorted by value - descending"""
    if lst==sorted(lst, reverse=True):
        return True
    else:
        return False

lst=[23, 20, 7, 5, 1]
lst1=[23, 29, 7, 5, 1]
lst2=[23, 20, 7, 7, 1]

if sorted_list(lst2)==True:
    print(f"The array {lst2} is sorted in descending order.")
else:
    print(f"The array {lst2} is NOT sorted in descending order.")

