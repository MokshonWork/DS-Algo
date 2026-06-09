# prob:1
def rec(x,n):
    if n== 0:
        return
    
    print(x)
    rec(x,n-1)

t = int(input("likhna:"))
i = int(input("likhna:"))
rec(t,i)

# prob:2 1--> n
def rec(n,i:int= 1):
    if i > n:
        return
    
    print(i)
    rec(n,i+1)
# -->  it's a head recursion
t = int(input("likhna:"))
rec(t)

# prob:tail 1--> n
def print_1_to_n(n, current=1):
    if current > n:
        return
    print(current)
    return print_1_to_n(n, current + 1)  # tail-recursive call

print_1_to_n(5)


#prob:3 n-->1
def rec(n,i:int=1):
    if i > n:
        return
    
    rec(n,i+1)
    print(i)
    
# -->  it's a tail recursion / backtracking
t = int(input("likhna:"))
rec(t)

#prob:4 n-->1 using head recursion
def rec(n):
    if n == 0:
        return

    print(n)
    rec(n-1)

    
# -->  it's a head
t = int(input("likhna:"))
rec(t)