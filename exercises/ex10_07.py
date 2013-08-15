def is_anagram(s, t):
    s = s.lower().replace(" ", "")
    t = t.lower().replace(" ", "")
    
    first = list(s)
    second = list(t)

    first.sort()
    second.sort()
    
    return first == second

print is_anagram("Mary", "Army")
print is_anagram("Jim Morrison", "Mr Mojo Risin")
print is_anagram("War", "Peace")
