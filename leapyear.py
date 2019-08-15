# python no. 2

def is_leap_year(x):
    if x % 4 == int(round(0)) and x % 100 != int(round(0)):
        print'Year ' + (str(x) + ', is a leap year.')
    elif x % 4 == int(round(0)) and x % 100 == int(round(0)) and x % 400 == int(round(0)):
        print'Year ' + (str(x) + ', is a leap year.')
    else:
        print'Year ' + (str(x) + ', is not a leap year.')

def check():
    year = input('Choose year: ')
    is_leap_year(year)

while 1 > 0:
    check()