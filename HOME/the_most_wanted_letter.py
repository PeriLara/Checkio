"""
You are given a text, which contains different english letters and punctuation symbols. You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".
Input: A text for analysis as a string.
Output: The most frequent letter in lower case as a string.
Precondition:
A text contains only ASCII symbols.
0 < len(text) ≤ 105
"""

from collections import Counter


def checkio(text):
    print(text)
    alphaB = "abcdefghijklmnopqrstuvwxyz"
    text = text.lower()
    letter2occ = Counter(text)
    
    l2o = [(value, key) for key, value in letter2occ.items() if key in alphaB]
    l2o = sorted(l2o,key=lambda x: x[0], reverse = True)
    best_occ = l2o[0][0]
    if len(l2o) > 1 and best_occ == l2o[1][0]:
        most_wanted = [key for value, key in l2o if value == best_occ] 
        return min(most_wanted)
    return l2o[0][1]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")