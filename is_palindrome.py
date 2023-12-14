# Checks if string is palindrome,anagram,check titlecase
from collections import Counter


def is_palindrome(word):
    rev_word = word[::-1]
    if (word == rev_word):
        print(f'{word} is palindrome')
    else:
        print(f'{word} is not palindrome')
        
def is_anagram(word1, word2):
    if Counter(word1) == Counter(word2):
        print(f'{word1} and {word2} are anagrams')
    else:
        print(f'{word1} and {word2} are not anagrams')
        
def check_for_title(word):
    if word.istitle():
        print(f'{word} is in tittle case')
    else:
        print(f'{word} should be {word.title()}')
        
if __name__ == "__main__":
    is_palindrome('eric')
    is_anagram('save', 'evas')
    check_for_title('eric mwakazi')