def is_sorted(t):

    for i in range(len(t) - 1):
        if t[i] > t[i+1]:
            return False
    return True
        
print is_sorted([1,2,2])
print is_sorted(['b','a'])
