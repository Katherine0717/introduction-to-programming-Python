"""CSC 161 Lab: Decision Control

Ningyuan Xiong
Lab Section TR 12:30-2:45pm
Spring 2019
"""

def date_check(year, mounth, date, year2, mounth2, date2):
    date_valid = 1
    date_invalid = 2
    if mounth2 in [1, 3, 5, 7, 8, 10, 12]:
        if date2 not in range(1, 32):
            mounth2 = date_invalid
        else:
            mounth2 = date_valid
    elif mounth2 in [4, 6, 9, 11]:
        if date2 not in range(1, 31):
            mounth2 = date_invalid
        else:
            mounth2 = date_valid
    elif mounth2 == 2:
        year2 = leap_year(year, mounth, date, year2, mounth2, date2)
        if year2 == 1:
            if date2 in range(1, 30):
                mounth2 = date_valid
            else:
                mounth2 = date_invalid
        elif year2 == 2:
            if date2 in range(1, 29):
                mounth2 = date_valid
            else:
                mounth2 = date_invalid
        else:
            mounth2 = date_invalid
    else:
        mounth2 = date_invalid
    return mounth2

def leap_year(year, mounth, date, year2, mounth2, date2):
    import math
    leap = 1
    not_leap = 2
    if year2 % 4 == 0:
        if year2 % 100 == 0:
            if year2 % 400 ==0:
                year2 = leap
            else:
                year2 = not_leap
        else:
            year2 = leap
    else:
        year2 = not_leap
    return year2

def main():
    print("This program accepts a date in the form month/day/year and outputs whether or not the date is valid")
    day = input("Please enter a date (mm/dd/yyyy):")
    day2 = day.split("/")
    year = day2[2]
    mounth = day2[0]
    date = day2[1]
    year2 = int(year)
    mounth2 = int(mounth)
    date2 = int(date)
    valid_invalid = date_check(year, mounth, date, year2, mounth2, date2)
    if valid_invalid == 1:
        print(day,"is valid.")
    elif valid_invalid == 2:
        print(day, "is not valid.")
    else:
        print(day,"is not valid")

main()

    
