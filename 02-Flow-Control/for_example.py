print('My name is')
for i in range(5): # the i is set to 0 and goes up to until 5
    print('Jimmy Five Times (' + str(i) + ')')

total = 0
for num in range(101):
    total = num + total

print(total)


for i in range(5): # the i is set to 0 and goes up to until 5
    print('Jimmy Five Times (' + str(i) + ')')

 # The range() function can also be called with three arguments.
 # The first two arguments will be the start and stop values, and the third will be the step argument.
 # The step is the amount that the variable is increased by after each iteration.
 # The range() function is flexible in the sequence of numbers it produces for for loops.
 # For example (I never apologize for my puns),
 # you can even use a negative number for the step argument to make the for loop count down instead of up.
for i in range(5, -1, -1):
    print(i)
