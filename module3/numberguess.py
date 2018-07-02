low = 0
high = 100
guess = 50
answer = 'clear'

guessQuestion = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."

print('Please think of a number between ' + str(low) + ' and ' + str(high) + '!\n')

while(answer != 'c'):
    if (answer == 'h'):
        high = guess
    elif (answer == 'l'):
        low = guess
    elif (answer != 'clear'):
        print('Sorry, I did not understand your input.')
    guess = int((low + high)/2)
    print('Is your secret number ' + str(guess) + '?')
    answer = input(guessQuestion)
print('Game over. Your secret number was:', guess)