M, D = map(int, input().split())

# Please write your code here.

day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def YesNo(M, D):
    if (M>=1 and M<=12) and (D<=day[M]):
        return True
    else:
        return False

if YesNo(M,D):
    print("Yes")
else:
    print("No")
    
