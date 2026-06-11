'''
1. pick a pivot
--> it can be first element
--> it can be last element
--> it can be middle element
--> it can be any random element

2. put pivot at its corect position/index
'''
nums = [4, 1, 7, 6, 3, 2, 8]

def partition(nums, low, high):
    pivot = nums[low]
    i = low
    j = high

    while i < j:

        while i <= high - 1 and nums[i] <= pivot:
            i += 1

        while j >= low + 1 and nums[j] > pivot:
            j -= 1

        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[low], nums[j] = nums[j], nums[low]
    return j

def quicksort(nums, low, high):
    if low < high:
        p = partition(nums, low, high)

        quicksort(nums, low, p - 1)
        quicksort(nums, p + 1, high)


