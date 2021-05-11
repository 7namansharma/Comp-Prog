n, h = map(int, input().split())
l = list(map(int, input().split()))
c = 0
for i in range(len(l)):
    if l[i] <= h:
        c += 1
    elif l[i] > h:
        c += 2
print(c)
