def letter_frequencies(filename):

    freq = {}
    output = []
    fin = open(filename).read()
        
    for char in fin:
        if char.isalpha():
            char = char.lower()        
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

    for key, value in freq.items():
        output.append((value, key))

    output.sort(reverse = True)

    for (count, letter) in output:
        print letter, count

letter_frequencies("pg1661.txt")
