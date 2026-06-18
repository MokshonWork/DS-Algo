# https://leetcode.com/problems/rotate-array/


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:# 1. brute force:
       n = len(nums)
       rotations = k%n
       for _ in range(0,rotations):
        e = nums.pop()
        nums.insert(0,e)

    def rot_slic(self, nums: list[int], k: int):# 2. slicing:
       n = len(nums)
       rotations = k%n
       nums[:] = nums[n-k:] + nums[:n-k]

    def rot_opt(self, nums: list[int], left,right):# 3.optimal method :
       while left < right:
          nums[left],nums[right] = nums[right],nums[left]
          left +=1
          right -=1
       
        
nums = [1,2,3,4,5,6,7]
k = 3
n =len((nums))
sol = Solution()      
# sol.rotate(nums, k)
# sol.rot_slic(nums,k)
# print(nums)

sol.rot_opt(nums,n-k,n-1)# rev last k elem
sol.rot_opt(nums,0,n-k-1)#rev rem elem
sol.rot_opt(nums,0,n-1) 
print(nums)

