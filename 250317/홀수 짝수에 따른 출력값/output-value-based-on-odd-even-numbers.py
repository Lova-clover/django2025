N = int(input())

# Please write your code here.

def func(N):
    if N==0:
        return 0
    if N==1:
        return 1

    if N%2==0:
        return func(N-2)+N
    if N%2!=0:
        return func(N-2)+N

print(func(N))