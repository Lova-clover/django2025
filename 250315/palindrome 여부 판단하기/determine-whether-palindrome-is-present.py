A = input()

# Please write your code here.

def palindrome(A):
    if A == A[::-1]:
        return True
    else:
        return False

if palindrome(A):
    print("Yes")
else:
    print("No")