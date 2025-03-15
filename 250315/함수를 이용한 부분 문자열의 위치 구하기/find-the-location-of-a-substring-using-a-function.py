text = input()
pattern = input()

def func():
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            return i
    return -1

print(func())

