nums = [5,3,9,8,1,6,4,-10,-100]

def linear_search(num:list[int],targeT:int):
    n = len(num)
    for i in range(0,n):
        if num[i] == targeT:
            print(i)

linear_search(nums,4) 