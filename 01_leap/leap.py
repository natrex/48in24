"""
A leap year (in the Gregorian calendar) occurs:

In every year that is evenly divisible by 4.
Unless the year is evenly divisible by 100, in which case it's only a leap year if the year is also evenly divisible by 400.
"""

years = [1000, 4, 3, 400, 100, 444, 2024]

def leap_year(year):
    if not year % 4 == 0:
        return False
    elif year % 100 == 0 and not year % 400 == 0: 
        return False
    else:   
        return True 


def main():
    for year in years: 
        print(year, leap_year(year))


main()