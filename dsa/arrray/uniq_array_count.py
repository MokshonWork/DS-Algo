nums = [1,1,1,2,3,4,4,7,9,9,9,10]

def uniq_arr_count(num:list):
    n = len(num)
    unique_array = {}

    for i in range(0,n):
        unique_array[num[i]] = 0

    print("Unique elemenst in an arr:")
    for i in unique_array:
        print(i,end=" ")
    print(" ")

    j = 0
    for k in unique_array:
        num[j] = k
        j+=1
    return j

# print(f"The unique count of elements in an array is :{uniq_arr_count(nums)}")

def uni_arr_count(data:list):
    n = len(data)
    if n ==1:
        return 1
    
    i = 0
    j = i+1
    while j<n:
        if data[j] != data[i]:
            i+=1
            data[i],data[j] = data[j],data[i]
        j+=1
    return i+1


print(f"The unique count of elements in an array is :{uni_arr_count(nums)}")
