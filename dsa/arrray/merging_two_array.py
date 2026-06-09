def merge_array(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


arr_lf = [1, 2, 3, 4]
arr_right = [1, 1, 3, 4, 5, 6, 7]

print(merge_array(arr_lf, arr_right))