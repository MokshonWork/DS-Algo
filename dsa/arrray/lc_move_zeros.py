#https://leetcode.com/problems/move-zeroes/description/

nums = [ 1,0,2,4,3,0,0,3,5,1]

class Solution:
    def moveZeroes(self, nums: list[int]) :
        n = len(nums)
        temp = []
        for i in range(0,n):
            if nums[i] !=0:
                temp.append(nums[i])

        n_temo = len(temp)
        for i in range(o,n_temo):
            nums[i] = temp[i]

        for i in range(n_temo,n):
            nums[i] =0
            


