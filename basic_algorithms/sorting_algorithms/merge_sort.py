def merge_sort(l):
    if len(l) < 2:
        return l
    middle = len(l) // 2
    sorted_left = merge_sort(l[:middle])
    sorted_right = merge_sort(l[middle:])
    return merge(sorted_left, sorted_right)

def merge(left, right):
    left_i = 0
    right_i = 0
    result = []
    while left_i < len(left) and right_i < len(right):
        if left[left_i] < right[right_i]:
            result.append(left[left_i])
            left_i = left_i + 1
        else:
            result.append(right[right_i])
            right_i = right_i + 1
    result.extend(left[left_i:])
    result.extend(right[right_i:])
    return result

L = [1, 5, 3, 8, 4, 9, 6, 2]
print(merge_sort(L))
