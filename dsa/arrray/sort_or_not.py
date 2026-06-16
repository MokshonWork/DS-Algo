nums = [1,3,5,7,9]

def sor_or_not(data:list):
    n = len(data)
    for i in range(0,n-1):#till last 2nd element
        if data[i] > data[i+1]:
            return False
    return True

print(sor_or_not(nums))