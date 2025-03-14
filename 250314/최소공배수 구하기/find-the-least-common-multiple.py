n, m = map(int, input().split())

# Please write your code here.

def nm(n,m):
    a = 0
    for i in range(1, min(n,m)+1):
        if n%i==0 and m%i==0:
            a = i
    print(n*m // a)

nm(n,m)
