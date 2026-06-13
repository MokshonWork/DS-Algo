def s_l(data):
    largest = float("-inf")
    sec_largest = float("-inf")
    n = len(data)

    for i in range(n):
        largest = max(largest, data[i])

    for i in range(n):
        if data[i] > sec_largest and data[i] != largest:
            sec_largest = data[i]

    return sec_largest

# nums = [55, 32, 97, -55, 45, 32, 88, 21]
# print(s_l(nums))


def se_l(data):
    largest = float("-inf")
    sec_largest = float("-inf")
    n = len(data)

    for i in range(0,n):
        if data[i] > largest:
            sec_largest = largest
            largest = data[i]
        elif data[i] > sec_largest and data[i] != largest:
            sec_largest = data[i]

    return sec_largest
        
nums = [55, 32, 97, -55, 45, 32, 88, 21]
print(se_l(nums))
