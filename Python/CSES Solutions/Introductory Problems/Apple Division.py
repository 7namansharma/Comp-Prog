import sys
n = int(input())
l = list(map(int, input().split()))
suml = sum(l)
ans = sys.maxsize
for i in range(1 << n):
    s = 0
    for j in range(n):
        if i & 1 << j:
            s += l[j]
        ans = min(ans, abs((suml-s)-s))
print(ans)
