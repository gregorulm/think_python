import time

def process_file():

    fin = open('words.txt')

    def append():
        result = []
        for line in fin:
            word = line.strip()
            result.append(word)
        return result

    def concatenate():      # significantly faster!
        result = []
        for line in fin:
            word = line.strip()
            result += [word]
        return result

    start = time.clock()
    append()
    end = time.clock()
    print "Append:\t\t", end - start

    start = time.clock()
    concatenate()
    end = time.clock()
    print "Concatenate:\t", end - start

process_file()
