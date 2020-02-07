"""
Write a function that finds the longest palindromic substring of a given string. Try to be as efficient as possible!
If you find more than one substring, you should return the one that’s closer to the beginning.
"""
def longest_palindromic(text):
    
    length = len(text)
    for i in reversed(range(length)):
        for j in range(length - i):
            sample = text[j:][:i+1]
            if sample == sample[::-1]:
                return sample

if __name__ == '__main__':
    
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"


