def rotate_word(s, shift):
    result = ""
    for char in s:
        result += chr((((ord(char) + (shift % 26)) % 123) % 97) + 97)
    return result

print rotate_word("cheer", 7)
print rotate_word("melon", -10)

