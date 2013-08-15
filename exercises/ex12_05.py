def metathesis_pairs():

    def create_dict():
        fin = open('words.txt')
        res = {}
        
        for line in fin:
            word = line.strip()
            res[word] = []

        return res

    def find_pairs(d):
        res = []
        
        for key, value in d.items():
            k = list(key)
            for i in range(len(key) - 1):
                for j in range(1, len(key)):
                    k[i], k[j] = k[j],  k[i]
                    candidate = make_string(k)
                    if candidate in d:
                        print key, candidate
        return res

    def make_string(k):
        res = ""
        for element in k:
            res += element
        return res
                    
    d = create_dict()
    find_pairs(d)

print metathesis_pairs()
