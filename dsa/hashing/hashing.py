'''
What is Hashing?

Hashing is a technique used to store and retrieve data quickly using a hash function.
Instead of searching through an array one by one, hashing lets us jump directly to the location where the data is stored.
'''
#Scan once, store information, answer forever.

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

'''
constraints:--> 1 <= n[i] <= 10
 --> n can have 10**8 elements
 --> m can have 10**8 elements
'''


'''
expected output:
10 → 1
111 → 0
1 → 1
9 → 0
5 → 4
67 → 0
2 → 2
'''

#brute force approach

for num in m:
    count = 0
    #iterating in both list it will make our
    # time comp: O(len(m) × len(n))
    for x in n:
        if x ==  num:
            count +=1
    
    print(num,count)# tle error confirmed 
    '''
    If:
      n = 10^8
      m = 10^8

    Then:
        10^8 × 10^8 = 10^16 operations
        Your computer will grow old before finishing.
    '''

# Hashing Idea:  instead of repeately searxhing n,
# let's count everything at once and stores it.
# create a freqauency array/hash map:

hash_lst = [0] *11

for num in n:
    hash_lst[num] +=1

for num in m:
    if num<0 or num >10:
        print(0)

    else:
        print(hash_lst[num]) 
#no tle error
'''
Time Complexity:
O(n + m)

Reason:
One traversal of n and one traversal of m.

Space Complexity:
O(11) = O(1)

Reason:
Hash array size is fixed (11 elements) and does not depend on input size.
'''


print(n)#1st list
print(m)#2nd list

freq = {} # empty dict for hashing

for nums in n:
    freq[nums] = freq.get(nums,1)+1

for x in m:
    if x<0 or x>10:
        print(freq.get(x,0))
    else:
        print(freq.get(x,nums))


