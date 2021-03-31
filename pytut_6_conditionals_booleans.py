#https://www.youtube.com/watch?v=DZwmZ8Usvnk&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=6

# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

language = 'Java'

if language == 'Python':
    print('Conditional Was True')
elif language == 'Java':
    print('Language is Java')
else:
    print('No match')

# and
# or
# not
 
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
     print('Admin Page')
else:
    print('Bad Creds')

if not logged_in:
    print('Please Log In')
else:
    print('Welcome')

a = [1, 2, 3]
#b = [1, 2, 3]
b = a
print(id(a))
print(id(b))
print(a is b)

condition = None

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

