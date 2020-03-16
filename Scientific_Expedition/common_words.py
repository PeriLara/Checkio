"""
Let's continue examining words. You are given two string with words separated by commas. Try to find what is common between these strings. The words are not repeated in the same string.
Your function should find all of the words that appear in both strings. The result must be represented as a string of words separated by commas in alphabetic order.
"""
def checkio(first, second):
    first = first.split(',')
    second = second.split(',')
    in_common = [element for element in first if element in second]
    in_common.sort()
    return ",".join(in_common)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"


