print("welcome to the exciting world of number guessing")
import random
number_to_guess = random.randint(1,100)
guess = int(input('Please guess a number between 1 and 100: '))
count_number_of_tries = 1

while number_to_guess!= guess:
    print("sorry , wrong number")
    if count_number_of_tries == 7:
        break
    elif guess < number_to_guess:
        print('Your guess was lower than the number')
    else:
        print('Your guess was higher than the number')
    guess = int(input('Please guess again: ')) #tbd...
    count_number_of_tries +=1

# Check to see if they did guess the correct number
if number_to_guess == guess:
    print('Well done you won!')
    print('You took', count_number_of_tries , 'tries to complete the game.ang galing galing')
else:
    print("Sorry - you lose. try gain next time")
    print('The number you needed to guess was', number_to_guess)
print('Game Over')