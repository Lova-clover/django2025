n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

ans = 0
# #가능한 모든 구간들에 대해
# # 구간의 시작점이 0 ~ n-k까지 일 때
# for i in range(n - k + 1):
#     # 구간 내의 합을 구한다
#     value = sum(arr[i:i+k])    

#     ans = max(ans, value)

for i in range(n-k+1):
    value = 0
    for j in range(i, i+k):
        value += arr[j]
    ans = max(ans, value)

print(ans)
