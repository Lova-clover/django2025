n, m = map(int, input().split())
a = 0

# Please write your code here.
def nm(n,m):
    for i in range(1, max(n,m)+1):
        if n%i==0 and m%i==0:
            a = i
    print(a)

nm(n,m)
