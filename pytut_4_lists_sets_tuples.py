# @author Delphik
# https://www.youtube.com/watch?v=W8KRzm-HUcc
courses = ['History', 'Math', 'Physics', 'Comp-Sci']
courses_2 = ['Art', 'Education']



nums = [1, 5, 2, 4, 3]

print(courses)
print(len(courses))
print(courses[3])
print(courses[-1])
print(courses[0:2])
print(courses[2:])
courses.append('Art')
print(courses)
courses.remove('Art')
courses.insert(0,'Art')
print(courses)
courses.remove('Art')
courses.insert(0,courses_2)
print(courses)
courses = ['History', 'Math', 'Physics', 'Comp-Sci']
courses.extend(courses_2)
print(courses)
print(courses.pop())
print(courses)
courses.reverse()
print(courses)
courses.sort()
#nums.sort()
print(courses)
print(nums)
print(sorted(nums))
print(min(nums))
print(max(nums))
print(sum(nums))
print(courses.index('Comp-Sci'))
print('Art' in courses)

for item in courses:
    print(item)
for index, course in enumerate(courses, start=1):
    print(index, course)

course_str = ', '.join(courses)
print(course_str)
new_list = course_str.split(' - ')
print(new_list)
print()
list_1 = ['History', 'Math', 'Physics', 'Comp-Sci']
list_2 = list_1

list_1[0] = 'Art'
print(list_1)
print(list_2)

# tuples

tuple_1 = ('History', 'Math', 'Physics', 'Comp-Sci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

#sets

cs_courses = { 'History', 'Math', 'Physics', 'Comp-Sci', 'Math'}
art_courses = { 'History', 'Math', 'Physics', 'Art', 'Design'}


print(cs_courses)
print('Math' in cs_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))


#empty structure

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()