""" Multiplication. Iterative & Recursive implementaion """

def mult_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

def mult_recurs(a, b):
    if b == 1:
        return a
    else:
        return a + mult_recurs(a, b-1)

for args in ((2,3), (3,4), (10, 10)):
    print(f'Iterative: {mult_recurs(args[0], args[1])}')
    print(f'Recursive: {mult_iter(args[0], args[1])}\n')


""" List elements multiplication """
def mult_list_recur(L):
    if len(L) == 1:
        return L[0]
    else:
        return L[0]*mult_list_recur(L[1:])

print(mult_list_recur([1,3,5,7,9]))
