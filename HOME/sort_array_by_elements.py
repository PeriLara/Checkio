"""
Sort the given iterable so that its elements end up in the decreasing frequency order, that is,
the number of times they appear in elements. 
If two elements have the same frequency, they should end up in the 
same order as the first appearance in the iterable.
Input: Iterable
Output: Iterable
Precondition: elements can be ints or strings
The mission was taken from Python CCPS 109 Fall 2018. 
It's being taught for Ryerson Chang School of Continuing Education by Ilkka Kokkarinen
"""

from collections import Counter, OrderedDict

def frequency_sort(items):

    if items == []:
        return []
    
    item2count = Counter(items)
    item2count_ordered = OrderedDict(sorted(item2count.items(), key=lambda t: t[1], reverse=True))
    
    res = ''
    for item, count in item2count_ordered.items():
        res += f'{str(item)} '*count
    try:
        return list(map(int, res.split()))
    except:
        return res.split()



if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
    print(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2], frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")

