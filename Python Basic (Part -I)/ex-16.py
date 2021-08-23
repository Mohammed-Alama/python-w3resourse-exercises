"""
Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
"""


number = int(input('Write number'))

if number > 17:
    result = (number - 17) * 2
else:
    result = 17 - number

print(result)
