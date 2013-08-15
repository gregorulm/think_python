import random

def birthday_paradox():

    def has_duplicates(t):
        return len(set(t)) < len(t)

    def month():
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", \
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        return months[random.randrange(12)]

    def day():
        days = [31, 28, 31, 30, 31, 30, \
                31, 31, 30, 31, 30, 31]
        if random.randrange(4) == 0:
            days[1] = 29
        return random.randrange(1, days[random.randrange(12)] + 1)

    def create_birthdays():
        birthdays = []
        for i in range(23):
            birthdays.append(month() + "-" + str(day()).zfill(2))
        return birthdays

    def matches():
        runs = 1000
        count = 0
        
        for i in range(runs):
            if has_duplicates(create_birthdays()):
                count += 1.0
        return count / runs

    return matches()


print birthday_paradox()
