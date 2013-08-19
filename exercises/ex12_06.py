def reduce_words():

    def create_dict():
        fin = open('words.txt')
        res = {}
        
        for line in fin:
            word = line.strip()
            res[word] = []
            
        for element in ["a", "i", ""]:
            res[element] = []

        return res

    def add_children(d):
        for key in d.keys():
            children = []
            for i in range(len(key)):
                candidate = key[:i] + key[i+1:]
                if candidate in d and candidate not in children:
                    children.append(candidate)
            d[key] = children
            
        return d

    def recursive_trails(d):
        res = []

        def helper(key, result):
            if d[key] == []:
                return
            if key in ["a", "i", ""]:
                res.append((len(result[0]), result))
            else:
                for entry in d[key]:
                    return helper(entry, result + [entry])
                
        for key,value in d.items():
            helper(key, [key])

        return res

    def top_n(results, n):
        results.sort(reverse = True)
        for i in range(n):
            print results[i]
                    
    d = create_dict()
    add_children(d)    # creates dictionary entries for words that are reducible
    trails = recursive_trails(d)
    top_n(trails, 20)

reduce_words()
