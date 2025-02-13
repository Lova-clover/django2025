arr = list(map(int, input().split()))
max_val = arr[0]
min_val = arr[0]

for elem in arr:
    if elem>max_val and elem != 999:
        max_val = elem
    
    if elem<min_val and elem != -999:
        min_val = elem
print(max_val, min_val)