nums = [55,32,-97,99,3,67]

#method 1

def l_S(data:list):
    largest_element = data[0]
    n = len(data)
    for i in range(0,n):
        if data[i] > largest_element:
            largest_element = data[i]
    return largest_element

# print(l_S(nums))


# method 2

def li_s(data:list):
    largest_element = data[0]
    n = len(data)
    for i in range(0,n):
        largest_element = max(largest_element,data[i])
    return largest_element

print(li_s(nums))



