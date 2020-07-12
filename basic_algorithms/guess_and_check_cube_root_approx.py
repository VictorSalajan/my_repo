cube = float(input('Enter the number whose cube root you want to find: '))
epsilon = float(input('How close do you want to be to the answer? (e.g.,: 0.01)\n'))
increment = float(input('Specify the amount you want to increment your guess with (e.g.,: 0.0001).\n'))

guess = 0.0
num_guesses = 0

while abs(guess**3 - abs(cube)) >= epsilon and guess <= abs(cube):
    guess += increment
    num_guesses += 1

print('num_guesses =', num_guesses)

if abs(guess**3 - abs(cube)) >= epsilon:
    print('Failed on cube root of', cube)
else:
    if cube < 0:
        guess = -guess
    print(guess, 'is close to the cube root of', cube)
