n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
mini = l[m-1] - l[0]
for i in range(m-n+1):
    mini = min(mini, l[i+n-1]-l[i])
print(mini)
