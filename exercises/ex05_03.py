def check_fermat(a, b, c, n):
    if n > 2:
        if a ** n + b ** n == c ** n:
            return "It seems that Fermat was wrong."
        else:
            return "No, that doesn't work."

def fermat_input():
    a = int(raw_input("Enter variable a: "))
    b = int(raw_input("Enter variable b: "))
    c = int(raw_input("Enter variable c: "))
    n = int(raw_input("Enter exponent n: "))
    print check_fermat(a, b, c, n)

#print check_fermat(1, 2, 3, 3)
fermat_input()
