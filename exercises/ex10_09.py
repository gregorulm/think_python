def remove_duplicates(t):
    result = []
    t.sort()

    if len(t) == 0:
        return []

    result.append(t[0])
    
    for i in range(len(t)):
        if t[i] != result[-1]:
            result.append(t[i])
    return result

print remove_duplicates([1,2,3,4])
print remove_duplicates([1,2,2,2,4])
print remove_duplicates([1,2,2,2])
print remove_duplicates([2,2,2])
print remove_duplicates([])
print remove_duplicates([4,5,3,4])
