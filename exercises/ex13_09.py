import string
import math

def zipfs_law():

    def create_dict():
        fin = open('pg1661.txt')
        res = {}
        
        for line in fin:
            line = line.lower()
            for c in string.punctuation:
                line = line.replace(c, " ")
            words = line.split()
            
            for word in words:                
                if word in res:
                    res[word] = res[word] + 1
                else:
                    res[word] = 1
        return res

    def create_ranks(d):
        res = []
        for key, value in d.items():
            res += [(value, key)]
        res.sort(reverse = True)
        return res

    def output(ranks):
        f = open("plot_res.csv", "w")
        for i in range(len(ranks)):
            line = str(math.log(ranks[i][0])) + ", " + str(math.log(i + 1)) + "\n"
            f.write(line)
        f.close()
                   
    d = create_dict()
    ranks = create_ranks(d)
    output(ranks)

zipfs_law()
