# The List Data Type
# A list is a value that contains multiple values in an ordered sequence.
# The term list value refers to the list itself
# (which is a value that can be stored in a variable or passed to a function like any other value),
# not the values inside the list value.

# Getting Sublists with
# spam[2] is a list with an index (one integer).

# spam[1:4] is a list with a slice (two integers).
spam = ['cat', 'nat', 'bat']
print(spam[1])
# nat

spam1 = [['cat', 'bat'], [10, 20, 30, 40, 50]]

print(spam1[0])
# ['cat', 'bat']

print(spam1[0][1])
# 'bat'

print(spam1[1][4])
#50

# Negative Indexes

spam2 = ['cat', 'nat', 'bat']
print(spam2[-1])
# bat

spam3 = ['cat', 'bat', 'rat', 'elephant']
print(spam[0:4])
#['cat', 'bat', 'rat', 'elephant']

print(spam[1:3])
#['bat', 'rat']

print(spam[0:-1])
#['cat', 'bat', 'rat']

spam = ['cat', 'bat', 'rat', 'elephant']
spam[:2]
# ['cat', 'bat']

spam[1:]
# ['bat', 'rat', 'elephant']

spam[:]
# ['cat', 'bat', 'rat', 'elephant']

#List Concatenation and List Replication

[1, 2, 3] + ['A', 'B', 'C']
#[1, 2, 3, 'A', 'B', 'C']

['X', 'Y', 'Z'] * 3
#['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
spam
[1, 2, 3, 'A', 'B', 'C']

# Deleting Values from a list
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print(spam)
#['cat', 'bat', 'elephant']

del spam[2]
print(spam)
#['cat', 'bat']

# The in and not in Operators
'howdy' in ['hello', 'hi', 'howdy', 'heyas']
#True
spam = ['hello', 'hi', 'howdy', 'heyas']
('cat' in spam)
#False
('howdy' not in spam)
#False
('cat' not in spam)
#True

# Working with Lists

for i in range(4):
    print(i)

print()
# same as

for i in [0, 1, 2, 3]:
    print(i)

print()
list1 = list(range(4))

for i in list1:
    print(i)

supplies = ['pen', 'pencil', 'pizza', 'flame-thrower']

for i in range(len(supplies)):
    item = supplies[i]
    print(f'Index: {i} in the supplies list is {item}')

list2 = list(range(-100, 110, 10))
print(list2)

# Multiple Assignment Trick

cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
# you could type this line of code:

cat = ['fat', 'orange', 'loud']
size, color, disposition = cat

#  you can also do
a , b = 'Alice', 'Bob'
a, b = b, a

print(a)
# 'Bob

print(b)
# Alice

# Augmented Assignment Operators
spam = 100
spam += 1
spam -= 1
spam *= 1
spam /= 1
spam %= 1


