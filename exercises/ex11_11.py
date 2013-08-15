def homophones_puzzler():
    
    def create_dict():
        fin = open('words.txt')
        result = {}
        for line in fin:
            word = line.strip()
            if len(word) == 5:
                result[word] = (word[1:], word[0] + word[2:])
        return result

    def create_pronunciation_dict():
        d = dict()
        fin = open('c06d.txt')
        for line in fin:

            # skip over the comments
            if line[0] == '#':
                continue

            t = line.split()
            word = t[0].lower()
            pron = ' '.join(t[1:])
            d[word] = pron
            
        return d
                    
    words = create_dict()
    p = create_pronunciation_dict()

    for elements in words.items():
        first = elements[0]
        second = elements[1][0]
        third = elements[1][1]
        if first in p and second in p and third in p:
            if p[first] == p[second] == p[third]:
                print first, second, third

homophones_puzzler()

"""

def read_dictionary(filename='c06d'):

    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d

if __name__ == '__main__':
    d = read_dictionary()
    for k, v in d.items():
        print k, v
"""
