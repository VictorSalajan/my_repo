cube = float(input("Enter the number whose cube root you want to find: "))
epsilon = float(input('How close do you want to be to the answer? (e.g.,: 0.01)\n'))
num_guesses = 0

low = 0
high = abs(cube)
guess = (high + low)/2.0

while abs(guess**3 - abs(cube)) >= epsilon and guess <= abs(cube):
    if guess**3 < abs(cube):
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print('num_guesses =', num_guesses)
if cube < 0:
    guess = -guess
print(guess, 'is close to the cube root of', cube)
