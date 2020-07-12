import random


def bogo_sort(L):
    tries = 0
    while L != sorted(L):
        random.shuffle(L)
        tries += 1
    return f'It took {tries} tries to sort list {L}.'


L = [2, 1, 3, 4]
print(bogo_sort(L))
