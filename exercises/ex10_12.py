def reverse_pair():
    
    def create_list():
        fin = open('words.txt')

        result = []
        for line in fin:
            word = line.strip()
            result += [word]
        return result

    def in_list(sorted_list, term):
        min = 0
        max = len(sorted_list) - 1
        
        while True:
            i = (min + max) / 2
            if max < min:
                return False
            if term == sorted_list[i]:
                return True
            elif term < sorted_list[i]:
                max = i - 1
            else:
                min = i + 1
    
    word_list = create_list()
    
    for word in word_list:
        if in_list(word_list, word[::-1]):
            print word, word[::-1]

reverse_pair()
