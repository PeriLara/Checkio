"""
Stephen's speech module is broken. This module is responsible for his number pronunciation. He has to click to input all of the numerical digits in a figure, so when there are big numbers it can take him a long time. Help the robot to speak properly and increase his number processing speed by writing a new speech module for him. All the words in the string must be separated by exactly one space character. Be careful with spaces -- it's hard to see if you place two spaces instead one.
"""
ZERO2NINE = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
TEN2NINE = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
TWENTY2HUNDRED = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

def checkio(number):
    
    def write(number, w_number):
        str_number = str(number)
        if len(str_number) == 3: # can't be more than 3
            hundred_number = int(str_number[0])
            w_number.append(f"{ZERO2NINE[hundred_number]} {HUNDRED}")
            return write(str_number[1:], w_number)
        elif len(str_number) == 2:
            if str_number[0] == "0":
                zero_number = int(str_number[1])
                if zero_number > 0:
                    w_number.append(ZERO2NINE[zero_number])
            elif str_number[0] == "1":
                w_number.append(TEN2NINE[int(str_number[1])])   
            else:
                ten_number = int(str_number[0]) - 2
                zero_number = int(str_number[1]) 
                w_number.append(f"{TWENTY2HUNDRED[ten_number]}")
                if zero_number > 0:
                    w_number.append(ZERO2NINE[zero_number])
        else:
            zero_number = int(str_number[0])
            if zero_number > 0:
                w_number.append(ZERO2NINE[zero_number])
        return w_number
    print(" ".join(write(number, [])))
    return " ".join(write(number, []))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
