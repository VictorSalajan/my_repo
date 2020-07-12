def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                L[j-1], L[j] = L[j], L[j-1]
    return L


L = [4, 3, 2, 1, 5, 6]
print(bubble_sort(L))
