def find_gcd(a:int, b:int) -> int:
    if a%b==0:
        return b
    else:
        return find_gcd(b, a%b)

print(find_gcd(56,12))