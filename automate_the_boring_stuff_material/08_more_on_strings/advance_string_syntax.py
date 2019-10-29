# Escape Characters

# \'
# Single quote
# \"
# Double quote
# \t
# Tab
# \n
# Newline (line break)
# \\
# Backslash

# raw strings
print(r'That is Carol\'s cat.')
# That is Carol\'s cat.

# Multiline Strings with Triple Quotes
# While you can use the \n escape character to put a newline into a string,
# it is often easier to use multiline strings.
# A multiline string in Python begins and ends with either three single quotes or three double quotes.
# Any quotes, tabs, or newlines in between the “triple quotes” are considered part of the string.
# Python’s indentation rules for blocks do not apply to lines inside a multiline string.
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')

# Indexing and Slicing Strings worth similar to lists
spam = 'Hello world!'
spam[0]
# 'H'
spam[4]
# 'o'
spam[-1]
# '!'
spam[0:5]
# 'Hello'
spam[:5]
# 'Hello'
spam[6:]
# 'world!'
spam = 'Hello world!'
fizz = spam[0:5]
fizz
# 'Hello'
