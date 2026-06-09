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

def merge_sort(arr):
    if len(arr) <=1:
        return arr
    
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr  = arr[mid:]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)

    return merge_array(left,right)
    

nums =[3,1,2,4,1,5,2,6,4]
print(merge_sort(nums))