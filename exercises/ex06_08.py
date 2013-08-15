def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print gcd(169, 13)
print gcd(14, 3)



    
