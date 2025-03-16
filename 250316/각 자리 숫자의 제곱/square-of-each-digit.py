N = int(input())

# Please write your code here.

def func(N):
    if N<10:
        return N * N
    
    return func(N//10) + (N%10)*(N%10)

print(func(N))
