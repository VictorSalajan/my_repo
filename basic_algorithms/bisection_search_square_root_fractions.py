import sys

x = float(input("Enter a fractional number (0 < x < 1): \n"))

if not (0 < x and x < 1):
    print('Invalid number.')
    sys.exit(1)

epsilon = 0.001

high = 1
low = x
ans = (high + low) / 2

numGuesses = 0

while abs(ans ** 2 - x) >= epsilon:
    print('high =', high, 'low =', low, 'ans =', ans)
    numGuesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2

print('numGuesses =', numGuesses)
print(ans, "is close to the square root of", x)
