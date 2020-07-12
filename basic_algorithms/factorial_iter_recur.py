def iter_fact(x):
    prod = 1
    for i in range(2, x+1):
        prod *= i
    return prod

def recurs_fact(n):
    if n == 1:
        return 1
    else:
        return n * recurs_fact(n-1)

for n in (3,4,5):
    print(recurs_fact(n))
    print(iter_fact(n), '\n')
