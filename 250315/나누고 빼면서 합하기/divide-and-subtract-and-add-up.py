n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
cnt = 0

def func():
    global cnt, m
    while True:
        if m==1:
            break
        else:
            if m%2!=0:
                m -=1
                cnt += m
            else:
                m // 2
                cnt += m

func()
print(cnt)
