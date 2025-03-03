dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

x, y = 0, 0

N = int(input())
for _ in range(N):
    dir_c, dist = map(str, input().split())
    dist = int(dist)
    
    if dir_c == 'E':
        dir_num = 0
    elif dir_c == 'S':
        dir_num = 1
    elif dir_c == 'W':
        dir_num = 2
    elif dir_c == 'N':
        dir_num = 3
    
    #for _ in range(dist):   #중간 과정을 보고싶으면 for문
        # x = x + dx[dir_num]
        # y = y + dy[dir_num]
    
    x = x + dist * dx[dir_num] #결과만 볼 것이면 dist만 곱하면 됌
    y = y + dist * dy[dir_num]

print(x,y)