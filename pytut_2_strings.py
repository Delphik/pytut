# @author Delphik
# https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=2
message = 'Hello World'
greeting = 'Hello'
name = 'Max'


new_message = message.replace('World','Universe')
print('hello world')
print(message)
print(message[0:4])
print(message.find('World'))
print(new_message)
print(greeting + ', ' + name)

#message = '{}, {}. Wecome!'.format(greeting, name)
message = f'{greeting}, {name}. Wecome!'
print(message)
#print(dir(name))
print(help(str))