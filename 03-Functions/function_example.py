def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')

def hello_length(name):
    print(len(name))
    print(name)

hello()
hello_length("Arvin")

print() #this would return a None datatype

def plusOne(number):
    return number + 1

print(plusOne(4))

#None is a type of valuetype

# However, keyword arguments are identified by the keyword put before them in the function call.
# Keyword arguments are often used for optional parameters.
# For example, the print() function has the optional parameters end
# and sep to specify what should be printed at the end of its arguments
# and between its arguments (separating them), respectively.

print('Hello', end=' ')
print('World')
# the output would look like this:
# Hello World

print('cats', 'dogs', 'mice')
# cats dogs mice
# But you could replace the default separating string by passing the sep keyword argument. Enter the following into the interactive shell:

print('cats', 'dogs', 'mice', sep=' and ')
# cats,dogs,mice


