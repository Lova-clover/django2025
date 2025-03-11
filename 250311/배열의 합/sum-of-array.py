for _ in range(4):
    arr = list(map(int, input().split()))
    a = 0
    for elem in arr:
        a += elem
    print(a)