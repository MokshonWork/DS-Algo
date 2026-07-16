num:int = int(input("enter the number:"))
count:int = 0
while num > 0:
    count+=1
    num = num // 10

print(count)

