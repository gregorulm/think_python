from datetime import datetime

# Part 1:
def current_day():
    weekdays = [ "Monday", "Tuesday", "Wednesday", "Thursday",
                 "Friday", "Saturday", "Sunday" ]
    today = datetime.today()
    return weekdays[today.weekday()]

#print current_day()


# Part 2:
def birthday(t):
    today = datetime.today()
    age = today.year - t.year
    print "Your age is", age
    
    normalized_birthday = datetime(today.year, t.month, t.day)
    delta = today - normalized_birthday

    print "Your next birthday is in",

    if delta.days > 0:
         print delta
    else:
        today_next_year = today.replace(year = today.year + 1)
        print today_next_year - normalized_birthday
        
#b = datetime(1990, 8, 14)
#birthday(b)


# Part 3:
def double_day(b1, b2):
    delta = b1 - b2
    double_day = b1 + delta
    return double_day

#b1 = datetime(2000, 2, 20)
#b2 = datetime(1990, 8, 14)
#print double_day(b1, b2)


