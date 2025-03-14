y = int(input())

# Please write your code here.

def year(y):
    if y%100==0 and y%400!=0:
        return False
    if y%4==0:
        return True
    
if year(y):
    print("true")
else:
    print("false")