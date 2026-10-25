def division():
    while True:
        try:
            a=int(input("Please enter the dividend: "))
            break
        except ValueError:
            print("The dividend has to be a number!")
            continue

    while True:
        try:
            b=int(input("Please enter the divisor: "))
            if b==0:
                print("The divisor cannot be a zero.")
                continue
            break
        except ValueError:
            print("The divisor has to be a number!")
            continue
    return a/b

print(division())
