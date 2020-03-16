"""
An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once. Two words are anagrams to each other if we can get one from another by rearranging the letters. Anagrams are case-insensitive and don't take account whitespaces. For example: "Gram Ring Mop" and "Programming" are anagrams. But "Hello" and "Ole Oh" are not.
You are given two words or phrase. Try to verify are they anagrams or not.
"""
import re

def verify_anagrams(first_word, second_word):
    
    first_word = list(filter(lambda x: x!= " ", list(first_word.lower())))
    second_word = list(filter(lambda x: x!= " ", list(second_word.lower())))
    for caractere in second_word:
        
        if caractere not in first_word:
            return False
        else:
            first_word.remove(caractere)
    if first_word != []:
        return False
    return True 

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Hell") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"



