# This is a Guess the Number game.
import random

guessesTaken = 0

print('Hello! Whatis your name?')
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinkin of a number between 1 and 20.')

for guessesTaken in range(6):
  print('Tkae a guess.')
  guess = input()
  guess = int(guess)
  
  if guess < number:
    print('Your guess is too low.')
  
  if guess > number:
    print('Your guess is too high.')
    
  if guess == number:
    break
    
if guess == number:
  guessesTaken = str(guessesTaken + 1)
  print('Good job, ' + myName + '! You guessed my numer in  ' + guessesTaken + ' guesses!')
  
if guess != number:
  number = str(number)
  print('Nope. the number I was thinking of was ' + number +'.')
  
  # Here we learn how to use variables, for loop and doing comparison with if statements.
  # we also used already learnt print and input functions. Here we also imported random library and learned to use new function random.
