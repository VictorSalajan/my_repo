secret_number = int(input("Enter your secret number (0 <= nr < 99): "))
low = 0
high = 100
guess_range = (low + high)//2

print("Please think of a number between 0 and 100!") 

while True:
    print('Is your secret number ', guess_range, '?', sep='')
    guess_check = input('Enter \'h\' to indicate the guess is too high. ' +
                        'Enter \'l\' to indicate the guess is too low. ' +
                        'Enter \'c\' to indicate I guessed correctly. ')
    if guess_check not in 'hlc' or guess_check == '':
        print('Sorry, I did not understand your input.')
    if guess_check == 'h':
        high = guess_range
    elif guess_check == 'l':
        low = guess_range
    elif guess_check == 'c':
        print('Game over. Your secret number was:', int(guess_range))
        break
    guess_range = (low + high)//2
