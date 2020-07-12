def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    Iter = min(a, b) 
    gcd = 1
    while Iter > 0:
        if a % Iter == 0 and b % Iter == 0:
            gcd = Iter
            break
        else:
            Iter -= 1
    return gcd

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

for args in [(2, 12), (9, 12), (17, 12), (99, 198)]:
    print(f'Iterative: gcd of {args} is: {gcdIter(args[0], args[1])}')
    print(f'Recursive: gcd of {args} is: {gcdRecur(args[0], args[1])}\n')
