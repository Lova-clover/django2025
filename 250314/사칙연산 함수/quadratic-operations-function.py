a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def sum1(a,c):
    return a+c
def sub1(a,c):
    return a-c
def mul1(a,c):
    return a*c   
def div1(a,c):
    return a/c 

if o=="+":
    print(f"{a} {o} {c} = {sum1(a,c)}")
elif o=="-":
    print(f"{a} {o} {c} = {sub1(a,c)}")
elif o=="/":
    print(f"{a} {o} {c} = {div1(a,c)}")
elif o=="*":
    print(f"{a} {o} {c} = {mul1(a,c)}")
else:
    print("False")