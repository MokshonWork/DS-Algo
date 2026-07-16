num = int(input("enter:"))
count = len(str(num))
temp = num
sum:int = 0

while( num!=0):
    d = num%10
    sum = sum + (d**count)
    num = num//10

if(sum == temp):
    print("armstrong")
else:
    print("not an armstrong")


