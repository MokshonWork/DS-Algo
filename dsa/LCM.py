# ''''''
# LCM : lowest common factor
# smallest non-zero common number,
# which is the multiple of both the numbers
# video link = https://youtu.be/6ykRY6bHVX0?si=g0kPZenFWjo7hFkN
# ''''''

def compute_lcm(num1,num2):
    # Find the greater of the two numbers
    if num1 > num2:
        higher = num1
    
    else: 
        higher = num2

    # Store the initial value to use for incrementing
    original_higher = higher

    # The LCM will be the first multiple of 'higher' that is also a multiple of the other number.
    while True:
        if(higher % num1 == 0 and higher % num2 == 0):
            print(f"The LCM of {num1} and {num2} is {higher}")
            break
        else:
        # Increment by the original higher value

            higher = higher + original_higher 


if __name__ == "__main__":
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    print(compute_lcm(num1,num2))



# other method usibg the gcd

def compute_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def compute_lcm(n1, n2):
    # The LCM is the product of the numbers divided by their GCD.
    lcm = (n1 * n2) // compute_gcd(n1, n2)
    print(f"The LCM of {n1} and {n2} is {lcm}")

# Take input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Call the function
compute_lcm(num1, num2)