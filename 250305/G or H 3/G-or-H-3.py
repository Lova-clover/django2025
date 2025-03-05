n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.

ans = 0
#모든 간으한 구간에 대해
#시작점이 1 ~ 10000-k 인 구간들에 대해 각각
for st in range(1, 10000-k+1):
    ed = st + k
    # 구간 [st, ed] 내의 G, H의 개수를 세서 점수를 구한다
    score = 0
    # 모든 G,H에 대해 구간 내에 있는지 확인한다.
    for i in range(n):
        if st <= x[i] <= ed:
            if c[i] =='G':
                score +=1
            else:
                score +=2
    ans = max(ans, score)
print(ans)