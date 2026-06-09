nums = [5,7,8,4,1,6,9,2 ]

def bubble_sort(data: list[int]) -> None:
    n = len(data)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]

bubble_sort(nums)
print(nums)


def bubble_sort(data: list[int]) -> None:
    n = len(data)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]


