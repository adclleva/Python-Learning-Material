imoprt copy

list('Hello')
 # ['H', 'e', 'l', 'l', 'o']
name = 'Zophie'
print('Zo' in name)
# True

for letter in name:
    print(letter)

# Mutable and Immutable Data Types
# strings in python are immutable

name = 'Zophie a cat'
newName = f'{name[0:7]} the {name[8:12]}'
print(name)
# Zophie a cat
print(newName)
# Zophie the cat

# References
# When you assign a list to a variable, you are actually assigning a list reference to the variable.
# A reference is a value that points to some bit of data, and a list reference is a value that points to a list.
# Variables carry references to a list

def eggs(cheese):
    cheese.append("Hello")

spam = [1, 2, 3]
eggs(spam)
print(spam)
# this displays [1, 2, 3, 'Hello']
# because the function calls to the same reference of the list instead of copying it directly to save data nd help it become faster
# just in case there's a large data that's stored

# you can use the copy module to create a deep copy of a list that is separate from the reference that it is "copying"

# Line conitnuation is a pretty cool concept

print('Four score and seven ' + \
      'years ago...')
# You can also split up a single instruction across multiple lines using the
# \ line continuation character at the end. Think of \ as saying,
#  “This instruction continues on the next line.” The indentation on the line after a
#  \ line continuation is not significant.

