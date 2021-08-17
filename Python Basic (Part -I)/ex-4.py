"""
Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""
import math

value = float(input("Please enter a radius:\n"))
result = math.pi * math.pow(value, 2)
print("Circle area is {}".format(result))
