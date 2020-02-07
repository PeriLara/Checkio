"""
Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
Your task is simple - convert the input date and time from computer format into a "human" format.
"""
def date_time(time: str) -> str:
    date, time = time.split(" ")
    month_conversion = {"01":"January","02":"February", "03":"March", "04":"April", 
                        "05":"May", "06":"June", "07":"July", "08":"August",
                        "09":"September", "10":"October", "11":"November", "12":"December"}
    res = ""
    day, month, year = date.split(".")
    day = day if day[0] != "0" else day[1]
    month = month_conversion[month]
    
    hours, minutes = time.split(":")
    hours = hours if hours[0] != "0" else hours[1]
    minutes = minutes if minutes[0] != "0" else minutes[1]
    _min = "minutes" if int(minutes) > 1 or int(minutes) == 0 else "minute"
    _hour = "hours" if int(hours) > 1 or int(hours) == 0 else "hour"
    return ' '.join([day, month, year, "year", hours, _hour, minutes, _min]) 

if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
