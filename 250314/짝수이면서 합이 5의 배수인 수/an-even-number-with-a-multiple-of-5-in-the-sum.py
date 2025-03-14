n = int(input())

# Please write your code here.

def val(n):
    return n%2==0 and (n//10 + n%10) %5==0

if val(n):
    print("Yes")
else:
    print("No")