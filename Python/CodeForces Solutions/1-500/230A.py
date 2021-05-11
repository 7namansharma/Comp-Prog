s, n = map(int, input().split())
l = []
for i in range(n):
    l.append(tuple(map(int, input().split())))
flag = True
#print(l)
for x, y in sorted(l):
    if s>x:
        s += y 
    else:
        flag = False
        break
if flag:
    print("YES")
else:
    print("NO")