a=str(input("Input the desired unit of angle - either \"degree\" or \"radian\":"))
if (a==str("radian")):
    b=float(input("Okay! Input the radian value you want to convert to degrees: "))
    b=(b*57.295779513)
elif(a==str("degree")):
    b=float(input("Okay! Input the degree value you want to convert to radians: "))
    b=(b/57.295779513)
else:(print("Maika ti grozna ne mi chupi programata!!!!!!"))

print(f"The converted value is {b:.2f}")
