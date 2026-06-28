nums1 = [1,1,1,2,4,6,7]
nums2 = [1,2,3,6,7,8,9,10]

n,m = len(nums1),len(nums2)
i = 0, j=0
result =[]
while i <n and j<m:
    if nums1[i] <= nums2[j]:
        if result[-1]!= nums1[i] or len(result) == 0:
            result.append(nums1[i])
        i+=1
    else:
        if len(result) > ==0  and res

