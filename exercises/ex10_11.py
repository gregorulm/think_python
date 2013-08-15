def create_list():
    fin = open('words.txt')

    result = []
    for line in fin:
        word = line.strip()
        result += [word]
    return result

def bisect(sorted_list, term):
    min = 0
    max = len(sorted_list) - 1
    
    while True:
        i = (min + max) / 2
        if max < min:
            return None
        if term == sorted_list[i]:
            return i
        elif term < sorted_list[i]:
            max = i - 1
        else:
            min = i + 1

#test = ["a", "b", "c", "d", "e", "f"]
#print bisect(test, "f")

word_list = create_list()

i = bisect(word_list, "owl")    # returns 70015
print word_list[i] == "owl"     # True

print bisect(word_list, "owwl") # returns None

