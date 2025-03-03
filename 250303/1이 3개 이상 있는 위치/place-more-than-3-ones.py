def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input())
arr = [list(map(int, input().split())) for i in range(n)]

answer = 0
for x in range(n):
    for y in range(n):
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not in_range(nx, ny):
                continue

            if arr[nx][ny] == 1:
                cnt +=1
        
        if cnt >= 3:
            answer += 1

print(answer)