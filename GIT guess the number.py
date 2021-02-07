import random

number = random.randint(1,15)

name_of_the_player = input('Enter your name here : ')

guess_the_number = 0

while guess_the_number < 6:
     
     guess = int(input())
     guess_the_number +=1

     if guess < number:
         print('You guessed low number ')
     if guess > number:
         print('You guesses high number')
     if guess == number:
         print('Congratulations!! You guessed the right number!')
         break
if guess == number:
    print('you guesses the number in ' + str(guess_the_number) + ' tries')
else:
    print('you failed to guess the number . The number was '+ str(number))