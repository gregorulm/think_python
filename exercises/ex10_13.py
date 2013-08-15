def interlocked_words(n):
    
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

    if n == 2:  
        for word in word_list:
            if in_list(word_list, word[::2]) \
               and in_list(word_list, word[1::2]):
                print word[::2], word[1::2], word

    elif n == 3:
        for word in word_list:
            if in_list(word_list, word[::3]) \
               and in_list(word_list, word[1::3]) \
               and in_list(word_list, word[2::3]):
                print word[::3], word[1::3], word[2::3], word
                                                                                                             
#interlocked_words(2)
interlocked_words(3)
