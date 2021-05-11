cplus = 0
cminus = 0
for _ in range(int(input())):
    s = input()
    if s.find('+') != -1:
        cplus += 1
    elif s.find('-') != -1:
        cminus += 1
print(cplus-cminus)
