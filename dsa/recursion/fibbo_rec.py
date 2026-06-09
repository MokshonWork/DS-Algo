def fibb(num:int)->int:
    if num == 0 or num ==1:
        return num
    return fibb(num-1)+fibb(num-2)

print(fibb(7))