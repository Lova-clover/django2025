s1, q = input().split()
q = int(q)
s = list(s1)

for i in range(q):
    a,b,c = input().split()
    a = int(a)
    if a == 1:
        temp = s[int(b)-1]
        s[int(b)-1] = s[int(c)-1]
        s[int(c)-1] = temp
        print("".join(s))
    elif a == 2:
        for i in range(len(s)):
            if b == s[i]:
                s[i] = c
        print("".join(s))



