nums = [1,0,3,4]

#brute force
def miss_no(arr:list):# linear search
    n = len(arr)
    for i in range(0,n+1):
        if i not in arr:
            return i
# print(miss_no(nums))

#better
def miss_no1(arr:list):# dict. or you cans say hashing
    hash_map = {}
    n = len(arr)
    for i in range(0,n+1):
        hash_map[i] = 0
    for num in arr:
        hash_map[num] = 1

    for key,value in hash_map.items():
        if value == 0:
            return key
        
# print(miss_no1(nums))


#optimal

def miss_no2(arr:list):
    n = len(arr)
    sum:int = 0
    for i in arr:
        sum +=i
    return ((n * (n+1)/2) - sum)#ap Sn formula is used
        
print(miss_no2(nums))

        