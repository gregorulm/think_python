def consecutive_double_letters():

    fin = open('words.txt')

    for line in fin:
        word = line.strip()
        for i in range(len(word)):
            if len(word) >= 6 and i < len(word) - 5 \
               and word[i] == word[i+1] \
               and word[i+2] == word[i+3] \
               and word[i+4] == word[i+5]:
                print word
        
consecutive_double_letters()
