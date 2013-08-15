def has_duplicates(t):
    result = {}
    for element in t:
        if element in result:
            return True
        else:
            result[element] = 1
    return False

print has_duplicates([1,2,3,4])
print has_duplicates([1,2,2,4])
