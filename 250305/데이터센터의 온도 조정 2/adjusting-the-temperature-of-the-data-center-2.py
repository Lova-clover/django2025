N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.

def output(t, T_a, T_b):
    # 선호 온도가 T_a ~ T_b 일 때
    # 현재 온도가 t라면
    # 얼마만큼의 작업량을 얻을 수 있는지 반환하는 함수
    if t < T_a:
        return C
    elif T_a <=t <= T_b:
        return G
    else:
        return H

ans = 0
# 0에서 1000까지 모든 범위에 대해 탐색
for t in range(0, 1001):
    total_output = 0
    # N개의 장비에 대해 각각 작업량을 계산하며 누적
    #python에서는 이게 더 좋음
    total_output = sum([
        output(t, T_a, T_b)
        for T_a, T_b in ranges
    ])

    ## 다른방법
    # for i in range(N):    
    #     total_output += output(t, ranges[i][0], ranges[i][1])
    
    ans = max(ans, total_output)
print(ans)
