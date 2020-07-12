def iterPower(base, exp):
    if exp == 0:
        return 1
    result = base
    while exp > 1:
        result *= base
        exp -= 1
    return result

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        return base * recurPower(base, exp-1)

for args in ((2, 0), (2, 3), (10, 10)):
    print(f'Iterative: {iterPower(args[0], args[1])}')
    print(f'Iterative: {recurPower(args[0], args[1])}\n')
