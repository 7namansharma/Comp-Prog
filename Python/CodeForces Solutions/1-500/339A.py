s = input()
l = []
ans = []
for i in range(0, len(s), 2):
     l.append(s[i])
l.sort()
for i in range(len(l)):
    print(l[i], sep="", end="")
    if i != (len(l)-1):
        print("+", sep="", end="")
