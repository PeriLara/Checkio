"""
Our new calculator is censored and as such it does not accept certain words. You should try to trick by writing a program to calculate the sum of numbers.
Given a list of numbers, you should find the sum of these numbers. Your solution should not contain any of the banned words, even as a part of another word.
The list of banned words are as follows:
sum
import
for
while
reduce
"""
def recursivity(data, res):
    if len(data) == 1:
        return res + data[0]
    return recursivity(data[:-1], data[-1] + res)


def checkio(data):
    return recursivity(data,0)
    
checkio([1,2,3])
