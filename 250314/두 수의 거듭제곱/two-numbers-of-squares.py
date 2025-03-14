a, b = map(int, input().split())

# Please write your code here.
def fuc(a,b):
    mul = a
    for _ in range(b-1):
        a *= mul
    return a
        
print(fuc(a,b))