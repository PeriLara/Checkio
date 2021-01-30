def sum_consecutives(a):
    # your code here
    res = []
    if a == res:
        return res
    sum_res = a[0]
    for i in range(1, len(a)):
        if a[i] == a[i-1]:
            sum_res += a[i]
        else:
            res.append(sum_res)
            sum_res = a[i]
    res.append(sum_res)
    return res


if __name__ == '__main__':
    print("Example:")
    #print(list(sum_consecutives([1, 1, 1, 1])))

    # These "asserts" are used for self-checking and not for an auto-testing
    #assert list(sum_consecutives([1, 1, 1, 1])) == [4]
    #assert list(sum_consecutives([1, 1, 2, 2])) == [2, 4]
    #assert list(sum_consecutives([1, 1, 2, 1])) == [2, 2, 1]
    #assert list(sum_consecutives([3, 3, 3, 4, 4, 5, 6, 6])) == [9, 8, 5, 12]
    assert list(sum_consecutives([1])) == [1]
    assert list(sum_consecutives([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")

