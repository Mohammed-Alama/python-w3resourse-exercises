"""
Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
"""
from datetime import *

exam_st_date = (11, 12, 2014)

print(datetime(exam_st_date[2], exam_st_date[1], exam_st_date[0]).__format__('%d/%m/%Y'))
