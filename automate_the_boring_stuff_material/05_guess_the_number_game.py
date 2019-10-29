#this is guess the number game
import random

print ('Hello, What is your name?')
name = input()

print(f'Well, {name}, I am thinking of a number between 1 and 20.')

secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7): # you have six guesses to make 
    print ('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print("Your guess is to high.")
    else:
        break # this condition is if you guess right

if guess == secretNumber:
    print(f'Good job {name}! You guessed my number in {guess} tries.')
else:
    print(f'Better luck next time, the secret number was {secretNumber}')
