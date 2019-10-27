def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("'Error: Invalid argument.")

print(spam(2))
print(spam(12))
print(spam(0)) # for this case you get the printed state and it returns 'None'
print(spam(1))

# this is good for input validation

def catsFunction():
    print("How many cats do you have?")
    num = input()

    try:
        if int(num) >= 4 and int(num) > 0:
            print('That is a lot of cats')
        elif int(num) < 0:
            print('You can have a negative number of cats?')
        else:
            print('That\'s not many cats')
    except:
        print('Please input a number')

catsFunction()