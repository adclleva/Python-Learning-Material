spam = 0
if spam < 5:
    print('Hello, world.')
    spam = spam + 1

spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1

# input validation

# break statements breaks out of the loop
# continue statements goes back to the loop

spam = 0

while spam < 5:
    spam += 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))