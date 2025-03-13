string = input()
LR = input()

for i in range(len(LR)):
    if LR[i] == "L":
        string = string[1:] + string[:1]
    elif LR[i] =="R":
        string = string[-1] + string[:-1]
    
print(string)
