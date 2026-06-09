# nums = [2, 9, 8, 3, 6, 7, 1, 4, 5]
# left = 0
# right = len(nums) - 1

# while left < right:
#     nums[left], nums[right] = nums[right], nums[left]
#     left += 1
#     right -= 1

# print(nums)



def reverse_array(arr, left, right):
    # Base case: stop when pointers meet or cross
    if left >= right:
        return

    # Swap the elements at left and right
    arr[left], arr[right] = arr[right], arr[left]

    # Recursive call for the remaining inner array
    reverse_array(arr, left + 1, right - 1)


# Driver code
nums = [2, 4, 1, 7, 6, 3, 8, 9, 5]

reverse_array(nums, 0, len(nums) - 1)

print(nums)

    