def rotate_pairs():
    
    def create_dict():
        fin = open('words.txt')
        result = {}

        for line in fin:
            word = line.strip()
            result[word] = word
        return result

    def rotate_word(s, shift):
        result = ""
        for char in s:
            result += chr((((ord(char) + (shift % 26)) % 123) % 97) + 97)
        return result

    def find_pairs():
        for word in words:
            
            all_rotations = []
            
            for i in range(1, 26):
                rotated = rotate_word(word, i)
                all_rotations += [rotated]

            for i in range(len(all_rotations)):
                if all_rotations[i] in words:
                    print word, i + 1, all_rotations[i]
                    
    words = create_dict()
    find_pairs()


rotate_pairs()

"""
def test(s, shift):
    def rotate_word(s, shift):
        result = ""
        for char in s:
            result += chr((((ord(char) + (shift % 26)) % 123) % 97) + 97)
        return result
    return rotate_word(s, shift)

print test("fit", 9)
print test("orc", -9)
"""
