#method 1 

num = int(input("enter: "))
result = []

for i in range(1,num+1):
    if num%i == 0:
        result.append(i)

print(result)

# method 2
num = int(input("enter: "))
result = []


for i in range(1,num//2):
    if num%i == 0:
        result.append(i)

result.append(num)

print(result)


#method 3
import math


n = int(input("Enter a number: "))

print("Factors are:")

# Find factors using square root method
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        print(i)

        # Print paired factor if different
        if i != n // i:
            print(n // i)