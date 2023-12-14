# Checks if string is palindrome
def is_palindrome(word):
    rev_word = word[::-1]
    if (word == rev_word):
        print(f'{word} is palindrome')
    else:
        print(f'{word} is not palindrome')
    
if __name__ == "__main__":
    is_palindrome('eric')