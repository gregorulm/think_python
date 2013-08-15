import math

def is_palindrome(s):
    return s == s[::-1]

print is_palindrome("abcd")
print is_palindrome("amanaplanacanalpanama")
