dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

x, y = 0,0
dir_num = 0

s = input()

for i in range(len(s)):
    if s[i] == 'F':
        x += dx[dir_num]
        y += dy[dir_num]
    elif s[i] == 'L':
        dir_num = (dir_num +1) % 4 
    elif s[i] == 'R':
        dir_num = (dir_num +3) % 4

print(x, y)