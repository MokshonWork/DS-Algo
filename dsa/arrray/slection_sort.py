nums = [5,7,8,4,1,6,9,2 ]

def selection_sort(data: list[int]) -> None:
    n = len(data)
    for i in range(0,n):
        min_index =i
        for j in range(i+1,n):
            if data[j] < data[min_index]:
                min_index = j
        
        data[i],data[min_index] = data[min_index],data[i]

selection_sort(nums)
print(nums)


