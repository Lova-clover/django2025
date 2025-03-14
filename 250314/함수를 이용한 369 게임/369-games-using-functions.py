a, b = map(int, input().split())

# Please write your code here.

def val(a,b):
    cnt = 0
    for i in range(a,b+1):
        if i%3==0 or i%10==3 or i%10==6 or i%10==9 or i//10==3 or i//10 == 6 or i//10 == 9:
            cnt+=1
    return cnt

print(val(a,b))
