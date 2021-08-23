"""
Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
"""
import calendar
month = int(input('Enter Month'))
year = int(input('Enter Year'))

print(calendar.month(year, month))
