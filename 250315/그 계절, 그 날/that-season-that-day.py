Y, M, D = map(int, input().split())

# Please write your code here.
day1 = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day2 = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def yun(Y):
    if Y%100==0 and Y%4==0 and Y%400==0:
        return True
    if Y%100==0 and Y%400!=0:
        return False
    if Y%4==0:
        return True

def season(Y, M, D):
    if yun(Y):
        if (M>=1 and M<=12) and (D<=day2[M]):
            if(M>=3 and M<=5):
                return "Spring"
            elif(M>=6 and M<=8):
                return "Summer"
            elif(M>=9 and M<=11):
                return "Fall"
            else:
                return "Winter"
        else:
            return -1
    else:
        if (M>=1 and M<=12) and (D<=day1[M]):
            if(M>=3 and M<=5):
                return "Spring"
            elif(M>=6 and M<=8):
                return "Summer"
            elif(M>=9 and M<=11):
                return "Fall"
            else:
                return "Winter"
        else:
            return -1

print(season(Y,M,D))
