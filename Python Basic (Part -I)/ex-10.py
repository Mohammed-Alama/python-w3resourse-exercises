"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615
"""

number = int(input('Enter your number '))

print(
    number +
    int("{}{}".format(number, number)) +
    int("{}{}{}".format(number, number, number))
)
