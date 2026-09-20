x = {"google", "fmi", "yahoo", "sofia"}
y = {"sofia", "varna", "burgas", "plovdiv"}
z = x.intersection(y)
x.intersection_update(y)
print(z)
print(x)

x = {"google", "fmi", "yahoo", "sofia"}
y = {"sofia", "varna", "burgas", "plovdiv"}
z = x.symmetric_difference(y)
x.symmetric_difference_update(y)
print(z)
print(x)