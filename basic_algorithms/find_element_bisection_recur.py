def bisect_search(L, e):
    """ Assumes L's elements are in ascending order
        Recursively implements bisection search
    """
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L)//2
        if L[half] > e:
            return bisect_search(L[:half], e)
        else:
            return bisect_search(L[half:], e)


def bisect_search_efficient(L, e):
    """ Makes bisection search more efficient,
        by not copying the list at each recursive call. 
    """
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)

L = [1,2,3,5,7,9,18,27]

print(bisect_search(L, 1))
print(bisect_search_efficient(L, 1))
