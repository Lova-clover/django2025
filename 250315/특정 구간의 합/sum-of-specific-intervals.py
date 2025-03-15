n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(m)]

# Please write your code here.

def func():
    for i in range(m):
        cnt = 0
        for j in range(queries[i][1] - queries[i][0] + 1):
            cnt += arr[queries[i][0]-1]
            queries[i][0] += 1

            if queries[i][0] == queries[i][1]+1:
                break
        print(cnt)

func()