num:int = int(input("enter:"))
rev:int = 0
temp = num

while num!=0:
    d = num%10
    rev = (rev*10)+d
    num = num//10

print(f"the reverse num is {rev}")

if(rev == temp):
    print(f"{temp} is palindrome")
else:
    print(f"{temp} is not palindrome")