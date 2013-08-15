def odometer_readings():

    def palindromic(s):
        return s == (s)[::-1]

    for i in range(100000, 1000000):

        if palindromic(str(i)[2:]) \
           and palindromic(str(i + 1)[1:]) \
           and palindromic(str(i + 2)[1:5]) \
           and palindromic(str(i + 3)):
            print i, i+1, i+2, i+ 3
        
odometer_readings()
