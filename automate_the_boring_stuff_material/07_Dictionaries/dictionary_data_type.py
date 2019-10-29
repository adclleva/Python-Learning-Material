# The Dictionary Data Type
# Like a list, a dictionary is a collection of many values.
#  But unlike indexes for lists, indexes for dictionaries can use many different data types,
#  not just integers. Indexes for dictionaries are called keys,
#  and a key with its associated value is called a key-value pair.
# Dictionaries are mutable

# Dictionaries are unordered unlike lists
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
eggs == ham
# True

# Checking Whether a Key or Value Exists in a Dictionary
spam = {'name': 'Zophie', 'age': 7}
'name' in spam.keys()
# True
'Zophie' in spam.values()
# True
'color' in spam.keys()
# False
'color' not in spam.keys()
# True
'color' in spam
# False

# you can use list methods on dictionaries
spam = {'color': 'red', 'age': 42}
print(spam.keys())
# dict_keys(['color', 'age'])

print(list(spam.keys()))
# ['color', 'age']

print(list(eggs.keys()))
# ['name', 'species', 'age']

for v in eggs.values():
    print(v)
# Zophie
# cat
# 8
print()

for k in eggs.keys():
    print(k)
# name
# species
# age

for k, v in eggs.items():
    print(k, v)
# name Zophie
# species cat
# age 8

# tuples are immutable lists
# in this case it returns a tuple of the key and value below
for i in eggs.items():
        print(i)
# ('name', 'Zophie')
# ('species', 'cat')
# ('age', '8')

# get() method
# It’s tedious to check whether a key exists in a dictionary before accessing that key’s value.
# Get() method that takes two arguments: the key of the value to retrieve
# and a fallback value to return if that key does not exist.
picnicItems = {'apples': 5, 'cups': 2}
'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
# 'I am bringing 2 cups.'
'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'
# 'I am bringing 0 eggs.'

# The setdefault() Method
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
# 'black'
print(spam)
# {'color': 'black', 'age': 5, 'name': 'Pooka'}
spam.setdefault('color', 'white')
# 'black'
print(spam)
# {'color': 'black', 'age': 5, 'name': 'Pooka'}
# The first time setdefault() is called, the dictionary in spam changes to {'color': 'black', 'age': 5, 'name': 'Pooka'}.
# The method returns the value 'black' because this is now the value set for the key 'color'.
# When spam.setdefault('color', 'white') is called next, the value for that key is not changed to 'white' because spam already has a key named 'color'.

