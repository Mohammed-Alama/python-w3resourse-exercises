"""
Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
Sample filename : abc.java
Output : java
"""

file_name = input('Enter file name ')

print('file extension: {}'.format(file_name.split('.')[-1]))
