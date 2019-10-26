# This program says hello and asks for my name.
print('Hello world!') # prints of the string

print('What is your name?')    # ask for their name

myName = input() # inputs always evaluates a string thus you would need to convert into a float or into to do some manupulation
print('It is good to meet you, ' + myName)
print('The length of your name is:')

print(len(myName)) # evaluates the length of the string

print('What is your age?')    # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.') # str and int  and float converts

# you can't do string cat on ints or floats

# floats and integers can equal to each other while strings and  numbers dont
print(1)