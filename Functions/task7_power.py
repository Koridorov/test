def user_input():
    a=float(input("Enter a number: "))
    return a


print(str(user_input()**int(user_input())).strip(".0"))
          