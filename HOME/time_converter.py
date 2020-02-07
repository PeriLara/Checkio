"""
You prefer a good old 12-hour time format. But the modern world we live in would rather use the 24-hour format and you see it everywhere. Your task is to convert the time from the 24-h format into 12-h format by following the next rules:
- the output format should be 'hh:mm a.m.' (for hours before midday) or 'hh:mm p.m.' (for hours after midday)
- if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.'

Input: Time in a 24-hour format (as a string).
Output: Time in a 12-hour format (as a string).
Precondition:
'00:00' <= time <= '23:59'
"""

def time_converter(time):
    assert len(time) == 5 and time[2] == ':', 'The time given is not of shape dd:dd'
    
    hour, minutes = time.split(':')
    hour = int(hour)

    if hour == 0:
        time = '12:' + minutes
        return time + ' a.m.'
    elif hour == 12:
        return time + ' p.m.'
    elif hour < 12:
        time = str(hour) + ':' + minutes
        return time + ' a.m.'

    return f'{str(hour - 12)}:{minutes} p.m.'

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")