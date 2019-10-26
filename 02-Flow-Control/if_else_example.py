name ='Bob'
age = 3000

if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')

# blank string is considered false
# 0 0/0 are also considered false

# you can use the bool function to determine what are truthy and falsey