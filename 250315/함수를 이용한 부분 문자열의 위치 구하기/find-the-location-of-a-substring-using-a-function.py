text = input()
pattern = input()

cnt = []
# Please write your code here.
def func():
    for i in range(len(text)-1):
        if text[i] == pattern[0] and text[i+1] == pattern[1]:
            cnt.append(i)
            return True
    return False

if func():
    print(cnt[0])
else:
    print(-1)

