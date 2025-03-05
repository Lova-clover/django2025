A = input()
L = len(A)
#모든 경우를 찾고 if문으로 조건을 통해 개수를 구함

cnt = 0
for i in range(L):
    for j in range(L): # 좀 더 줄이려면 for j in range(i+1, L):
        # i < j and A[i] == '(' A[j] ==')' 일 때 개수 세주기
        if i < j and A[i] == '(' and A[j] == ')' :
            cnt +=1

print(cnt)