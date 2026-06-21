#https://leetcode.com/problems/move-zeroes/description/

nums = [ 1,0,2,4,3,0,0,3,5,1]

class Solution:
    def moveZeroes(self, nums: list[int]) :#-> brute
        n = len(nums)
        temp = []
        for i in range(0,n):
            if nums[i] !=0:
                temp.append(nums[i])

        n_temo = len(temp)
        for i in range(0,n_temo):
            nums[i] = temp[i]

        for i in range(n_temo,n):
            nums[i] =0
    
    def move_Zeroes(self, nums: list[int]) :#-> OPTIMAL
        if len(nums) ==1:
            return
        i = 0
        while i < len(nums):
            if nums[i] ==  0:
                break
            i+=1
        if i ==len(nums):
            return
        j=i+1
        while j<len(nums):
            if nums[j]!=0:
                nums[i],nums[j]= nums[j],nums[i]
                i+=1
            j+=1

sol = Solution()      
sol.moveZeroes(nums)
# print(nums)

sol.move_Zeroes(nums)
print(nums)




