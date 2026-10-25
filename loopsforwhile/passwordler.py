j=False
while True:
    password=str(input("Please enter your password: "))
    if len(password)<8:
        print("The password is too short. Please enter at least 8 characters.")
    
        continue
    else:
        for char in password:
            if char.isdigit():
                j=True
        if j==False:
            print("The password has to contain at least one digit.")
            continue
        else: 
            break
print("Your password has been saved. Thank you. ") 