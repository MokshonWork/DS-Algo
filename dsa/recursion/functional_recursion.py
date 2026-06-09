# sum till n number using the paramerised recusrion

def sum_till_n(n:int,sum:int = 0,i:int =1):
    if i > n:
        print(sum)
        return
    return sum_till_n(n,sum+i,i+1)

sum_till_n(5)


    
# sum till n number using the functinol recusrion

def sum_till_n(n):
    if n==1:
        return 1
    return (n+sum_till_n(n-1))

print(sum_till_n(5))


    
