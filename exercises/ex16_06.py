# Part 1:
    
class Time(object):
    """
    Represents the time of day.
    attributes: hour, minute, second
    """

def time_to_sec(t):
    hours = t.hour * 3600
    minutes = t.minute * 60
    seconds = t.second
    return hours + minutes + seconds

def sec_to_time(s):
    t = Time()
    t.hour = s / 3600
    t.minute = (s % 3600) / 60
    t.second = s % 60
    return t

def multiply_time(t, a):
    seconds = a * time_to_sec(t)
    return sec_to_time(seconds)


# Part 2:

def time_per_mile(t, miles):
    sec = time_to_sec(t) / miles
    return sec_to_time(sec)
