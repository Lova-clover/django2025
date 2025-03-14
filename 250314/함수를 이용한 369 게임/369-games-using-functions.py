a, b = map(int, input().split())

# Please write your code here.

def val(a,b):
    cnt = 0
    for i in range(a,b+1):
        i = str(i)
        bol = False
        for j in range(len(i)):
            if i[j] == '3' or i[j] == '6' or i[j] == '9'or int(i)%3 == 0:
                bol = True
        if bol == True:
            cnt +=1  
    return cnt

print(val(a,b))
