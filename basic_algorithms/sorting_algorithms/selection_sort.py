def selection_sort(L):
    for i in range(len(L) - 1):
        j = i + 1
        while j < len(L):
            if L[j] < L[i]:
                L[i], L[j] = L[j], L[i]
            j += 1
    return L

L = [1, 5, 3, 8, 4, 9, 6, 2]
print(selection_sort(L))
