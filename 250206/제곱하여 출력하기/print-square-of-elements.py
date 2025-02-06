n = int(input())
new_arr = []

a = list(map(int, input().split()))
for elem in a:
    new_arr.append(elem * elem)

for i in range(n):
    print(new_arr[i],end=" ")





    
    