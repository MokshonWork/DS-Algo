'''
character hashing: it works on the the same logic of normal hashing.
that we discussed earlier
'''

#brute force

# s = "azyxyyzaaaa" # note this all are in small letter(theref, range is 97 --> 122)
# q = ["d","a","y","x"]

# for char in q:
#     count = 0

#     for check in s:
#         if check == char:
#             count +=1
    
#     print(char,count)

# Hashing Idea:  instead of repeately searxhing n,
# let's count everything at once and stores it.
# create a freqauency array/hash map:

hash_list = [0]*26
s = "azyxyyzaaaa" 
q = ["d","a","y","x"]

for char in s:
    ass = ord(char)
    index = ass - 97
    hash_list[index] +=1

for fuck in q:
    fork = ord(fuck)
    index = fork - 97
    if fork <97 or fork >122:
        hash_list[index] = 0
    else:
        print(hash_list[index])


