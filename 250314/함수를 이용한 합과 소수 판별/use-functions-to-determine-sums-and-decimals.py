a,b = map(int,input().split())

def check(num):
    for a in range(2,num//2+1):
        if num%a == 0:
            return False
    scheck = 0
    while num != 0:
        scheck += num%10
        num = num//10
    if scheck%2 != 0:
        return False
    return True

ans = 0

for t in range(a,b+1):
    if check(t):
        ans += 1

print(ans)

