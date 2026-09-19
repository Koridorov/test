n=int(input("PLease enter your number of items: "))
undereight=[]
overeight=[]

for i in range (0,n):
    while True:
        primes=int(input("Please enter your prime numbers one by one: "))
        x=int(primes**(1/2)+1)
        #ne bachka za 3????
        isprime=False
        for j in range(2,x):
            if (primes%j!=0) and (primes<8):
                isprime=True
            elif (primes%j!=0) and (primes>8):
                isprime=True
            else:
                print("The number is not prime. Please enter a prime number.")
        if (isprime==True) or primes==3:
            if primes<8:
                undereight.append(primes)
            else:
                overeight.append(primes)
            break
print(f"""Primes entered under eight: {undereight}
Primes entered over eight: {overeight}""")
        
