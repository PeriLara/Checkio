"""
You are the modern man who prefers the 24-hour time format. But the 12-hour format is used in some places. Your task is to convert the time from the 12-h format into 24-h by following the next rules:
- the output format should be 'hh:mm'
- if the output hour is less than 10 - write '0' before it. For example: '09:05'
"""
def time_converter(time):
    hour, apm = time.split(" ")
    if hour[1] == ":": hour = "0"+hour
    if "a.m" in apm and hour != "12:00": return hour
    elif "a.m" in apm and hour == "12:00": return "00:00"
    else:
        if hour[:2] == "12": return hour
        else: return str(int(hour[:2]) + 12)+hour[2:]


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30 p.m.'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    print("Coding complete? Click 'Check' to earn cool rewards!")
