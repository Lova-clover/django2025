n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
cnt = 0

def func():
    global cnt, m
    cnt += A[m-1]
    while True:
        if m==1:
            break
        if m%2!=0:
            m -=1
            cnt += A[m-1]
        else:
            m = m // 2
            cnt += A[m-1]

func()
print(cnt)
