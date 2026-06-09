# def is_palindrome(s):
#     left = 0
#     right = len(s) - 1

#     while left < right:
#         if s[left] != s[right]:
#             return False

#         left += 1
#         right -= 1

#     return True


# print(is_palindrome("nitin"))

def fun(s:str,l:int,r:int):
    if l >= r:
        return True
    if s[l] != s[r]:
        return False
    return fun(s,l+1,r-1)

print(fun("nitin",0,4))
    