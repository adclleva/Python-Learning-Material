# Methods
# A method is the same thing as a function, except it is “called on” a value.
# For example, if a list value were stored in spam, you would call the index() list method (which I’ll explain next) on that list like so: spam.index('hello').
# The method part comes after the value, separated by a period.

# index method
spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello')
# 0
spam.index('heyas')
# 3

# append() and insert()
spam = ['cat', 'dog', 'bat']
spam.append('moose')
spam
# ['cat', 'dog', 'bat', 'moose']

spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
spam
# ['cat', 'chicken', 'dog', 'bat']

# Removing Values from Lists with remove()
# It would remove the first instance
spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat')
spam
# ['bat', 'rat', 'cat', 'hat', 'cat']

# Sorting the Values in a List with the sort() Method
spam = [2, 5, 3.14, 1, -7]
spam.sort()
spam
# [-7, 1, 2, 3.14, 5]

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
spam
# ['ants', 'badgers', 'cats', 'dogs', 'elephants']

# You can also pass True for the reverse keyword argument to have sort() sort the values in reverse order.
#  Enter the following into the interactive shell:
# Sorting happens in ASCII-betical order
spam.sort(reverse=True)
spam
['elephants', 'dogs', 'cats', 'badgers', 'ants']
