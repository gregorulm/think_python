import math

def estimate_pi():

    second_term = 0.0
    k = 0
    
    while True:
        num = math.factorial(4.0 * k) * (1103 + 26390 * k)
        denom = math.pow(math.factorial(k), 4) * math.pow(396, 4 * k)
        second_term += (num / denom)
        if (num / denom) < 1e-15:
            break
        k += 1
        
    return ((2 * math.sqrt(2)) / 9801) * second_term

print estimate_pi(), 1 / math.pi
    
