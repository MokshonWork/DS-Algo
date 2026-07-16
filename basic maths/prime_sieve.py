def prime_sieve(n):
    prime = [0 for i in range(101)]
    for i in range(2,n+1):
        if prime[i]==0:
            for j in range(i*i,n+1,i):
                prime[j] == 1
    
    for i in range(2,n+1):
        if prime[i]==0:
            print(i, end ='  ')

rng = int(input("Enter the no. till where you want to print the primes: 50"))
prime_sieve(rng)
