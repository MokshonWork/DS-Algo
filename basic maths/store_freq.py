# first method
'''
time complexity: o(n)
space complexity: o(n)
'''

nums = [5,6,7,7,1,9,111,1,1,6,5,1,1]

frq_map = dict()

for i in range(0, len(nums)): # --> o(n)
    if nums[i] in frq_map: # --> o(1)
        frq_map[nums[i]] += 1
    else:
        frq_map[nums[i]] = 1 # o(1)

user_num = int(input("enter the number"))

print(frq_map[user_num] )


# second method
'''
time complexity: o(n)
space complexity: o(n)
'''
nums = [5,6,7,7,1,9,111,1,1,6,5,1,1]

frq_map = {}

for num in nums:
    frq_map[num] = frq_map.get(num, 0) + 1


user_num = int(input("enter the number"))
print(frq_map[user_num] )

# 3rd method
'''
time complexity: o(n)
space complexity: o(n)
'''
nums = [5,6,7,7,1,9,111,1,1,6,5,1,1]

frq_map = {}
n = len(nums)

for i in range(0,n):
    frq_map[nums[i]] = frq_map.get(nums[i],0) + 1


user_num = int(input("enter the number"))
print(frq_map[user_num] )