# string methods

# The upper(), lower(), isupper(), and islower() String Methods

spam = 'Hello world!'
spam = spam.upper()
spam
# 'HELLO WORLD!'
spam = spam.lower()
spam
# 'hello world!'

spam = 'Hello world!'
spam.islower()
# False
spam.isupper()
# False
'HELLO'.isupper()
# True
'abc12345'.islower()
# True
'12345'.islower()
# False
'12345'.isupper()
# False

# isalpha() returns True if the string consists only of letters and is not blank.
# isalnum() returns True if the string consists only of letters and numbers and is not blank.
# isdecimal() returns True if the string consists only of numeric characters and is not blank.
# isspace() returns True if the string consists only of spaces, tabs, and new-lines and is not blank.
# istitle() returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.

'hello'.isalpha()
# True
'hello123'.isalpha()
# False
'hello123'.isalnum()
# True
'hello'.isalnum()
# True
'123'.isdecimal()
# True
'    '.isspace()
# True
'This Is Title Case'.istitle()
# True
'This Is Title Case 123'.istitle()
# True
'This Is not Title Case'.istitle()
# False
'This Is NOT Title Case Either'.istitle()
# False

# The startswith() and endswith() String Methods
'Hello world!'.startswith('Hello')
# True
'Hello world!'.endswith('world!')
# True
'abc123'.startswith('abcdef')
# False
'abc123'.endswith('12')
# False
'Hello world!'.startswith('Hello world!')
# True
'Hello world!'.endswith('Hello world!')
# True

#The join() and split() String Methods
', '.join(['cats', 'rats', 'bats'])
# 'cats, rats, bats'
' '.join(['My', 'name', 'is', 'Simon'])
# 'My name is Simon'
'ABC'.join(['My', 'name', 'is', 'Simon'])
# 'MyABCnameABCisABCSimon'i

print('My name is Simon'.split())
# ['My', 'name', 'is', 'Simon']
print('MyABCnameABCisABCSimon'.split('ABC'))
# ['My', 'name', 'is', 'Simon']
print('My name is Simon'.split('m'))
# ['My na', 'e is Si', 'on']

# Justifying Text with rjust(), ljust(), and center()
'Hello'.rjust(10)
# '     Hello'
'Hello'.rjust(20)
# '               Hello'
'Hello World'.rjust(20)
# '         Hello World'
'Hello'.ljust(10)
# 'Hello     '
'Hello'.center(20)
'Hello'.rjust(20, '*')
# '***************Hello'
'Hello'.ljust(20, '-')
# 'Hello---------------'
# '       Hello       '
'Hello'.center(20, '=')
# '=======Hello========'

# Removing Whitespace with strip(), rstrip(), and lstrip()
spam = '    Hello World     '
spam.strip()
# 'Hello World'
spam.lstrip()
# 'Hello World '
spam.rstrip()
# '    Hello World'
spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS')
# 'BaconSpamEggs'

spam = 'Hello there!'
spam.replace('e', 'XYZ')
# 'HXYZllo thXYZrXYZ!'

# Copying and Pasting Strings with the pyperclip Module
# pyperclip.copy('Hello world!')
# pyperclip.paste()
# 'Hello world!'
