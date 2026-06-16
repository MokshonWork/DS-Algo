nums = [5, -2, 3, 9, 0, 6, 10, 7]

def rotate_arr_1(num: list):
    n = len(num)
    # num[:] = [num[-1]] + num[0:n-1]
    num[:] = [num[n-1]] + num[0:n-1]

    return num

# print(rotate_arr_1(nums)) 

def rotate_arr_2(num: list):
    n = len(num)
    temp = nums[n-1]
    for i in range(n-2,-1,-1):
        num[i+1] = num[i]
    num[0] = temp
    return num

print(rotate_arr_2(nums)) 