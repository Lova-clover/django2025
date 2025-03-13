N = int(input())
sum_val = 0

for _ in range(N):
    a = int(input())
    sum_val += a
sum_val = str(sum_val)
sum_val = sum_val[1:] + sum_val[:1]

print(sum_val)