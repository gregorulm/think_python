def is_palindrome(word):
    
    def first(word):
        return word[0]

    def last(word):
        return word[-1]

    def middle(word):
        return word[1:-1]

    if len(word) <= 1:
        return True
    else:
        if first(word) == last(word):
            return is_palindrome(middle(word))
        else:
            return False

print is_palindrome("nope")
print is_palindrome("amanaplanacanalpanama")
