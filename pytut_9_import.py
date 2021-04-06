# https://www.youtube.com/watch?v=CqvZ3vGoGs0&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=9
import random
import sys
import math
import os
import datetime
import antigravity
import calendar

sys.path.append('/home/maxh/Python/My-Modules/')


from my_module import find_index, test
# from my_module import *
# import my_module as mm

courses = ['History', 'Math', 'Physics', 'Comp-Sci']

# index = mm.find_index(courses, 'Math')
index = find_index(courses, 'Math')
 
print(index)
print(test)
print(sys.path)

rads = math.radians(90)

print(random.choice(courses))
print(math.sin(rads))
print(datetime.date.today())
print(calendar.isleap(2021))
print(os.getcwd())
print(os.__file__)
