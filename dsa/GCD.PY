'''
video link = https://youtu.be/cahuG1cEQdY?si=GnYMjLk8jdyuM58C
Greatest common divisor
euclid's method: num1 = num2 * x +  remainder

example: num1 = 64, num2 = 48
therefore our equation will be --> 64 = 48 *x +remainder

64 = 48*1 +16
48 = 16*3 + 0
16 = 0

'''
def compute_gcd(num1,num2):

    
    if num2 == 0:
        return num1      

    else:
        return compute_gcd(num2,num1%num2)
    
if __name__ == "__main__":
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    print(compute_gcd(num1,num2))

# simple method

def compute_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

                