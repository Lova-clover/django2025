input_str, q = input().split()
q = int(q)

for _ in range(q):
    n = int(input())
    if n==1:
        input_str = input_str[1:] + input_str[:1]
        print(input_str)
    elif n==2:
        input_str = input_str[-1] + input_str[:-1]
        print(input_str)
    elif n==3: 
        print(input_str[::-1])
        
