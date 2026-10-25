symbol=str(input("Enter your symbol here: "))
#if symbol=="a" or symbol=="o" or symbol=="i" or symbol=="e" or symbol=="u" or symbol=="A" or symbol=="O" or symbol=="I" or symbol=="E" or symbol=="U":
#    print(f"{symbol} is a vowel")
#else: print(f"{symbol} is a consonant")
if symbol.lower() in "aoieu":
    print(f"{symbol} is a vowel.")
else:
    print(f"{symbol} is not a vowel.")