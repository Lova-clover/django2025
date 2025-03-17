a, b, c = map(int, input().split())

# Please write your code here.
d = a*b*c
def func(d):

    if d<10:
        return d
    
    return func(d//10) + d%10

print(func(d))