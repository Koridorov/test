a=int(input("Please enter the first number \"a\": "))
b=int(input("Please enter the second number \"b\": "))
c=int(input("Please enter the third number \"c\": "))
D=b**2-4*a*c
if a==0:
    print("With \"а\" equalling 0, it is no longer a quadratic equation.")
elif D<0:
    print("There are no real number solutions for this equation.")
else:
    x1=(-b+D**(1/2))/(2*a)
    x2=(-b-D**(1/2))/(2*a)
    print(f"The possible solutions are {x1}, {x2}")
