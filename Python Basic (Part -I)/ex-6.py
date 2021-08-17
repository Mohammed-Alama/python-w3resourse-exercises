"""Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a
tuple with those numbers  3, 5, 7, 23"""

numbers = input('Enter sequence of numbers')
numbers = numbers.split(',')
print("List :{}".format(list(numbers)))
print("Tuple :{}".format(tuple(numbers)))
