# @author Delphik
# https://www.youtube.com/watch?v=daefaLgNkw0&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=5

student = {'name': 'Jon', 'age': 25, 'courses': ['Math', 'Conp-Sci']}
print(student)
print(student['name'])
student['phone'] = '555-555-5555'
student['name'] = 'Jane'
print(student.get('phone', 'Not Found'))
student.update({'name': 'Jane', 'age': 26, 'phone': '555-555-5553'})
print(student)
# del student['age']
print(student.pop('age'))
print(student.keys())
print(student.items())

for key, value in student.items():
        print(key, value)