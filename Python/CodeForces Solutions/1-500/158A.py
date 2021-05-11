n, k = map(int, input().split())
l = list(map(int, input().split()))
c = 0
for i in range(n):
    if (l[i] >= l[k-1]) and (l[i] > 0):
        c += 1
print(c)