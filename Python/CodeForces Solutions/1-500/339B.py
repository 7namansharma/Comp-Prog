n, m = map(int, input().split())
l = []
l = list(map(int, input().split()))
pos = 1
ans = 0
for i in l:
    if pos<=i:
        ans += (i-pos)
        pos = i
    else:
        ans += (n-pos) + i
        pos = i
print(ans)

