import sys
n, m = map(int, input().split())
tick = list(map(int, input().split()))
cust = list(map(int, input().split()))
tick.sort()
for i in range(m):
    j = n - 1
    flag = False
    diff = sys.maxsize
    while j >= 0:
        if tick[0] > cust[i]:
            break
        if cust[i] >= tick[j]:
            diff = cust[i] - tick[j]
            flag = True
            break
        j -= 1
    if not flag:
        print(-1)
    else:
        print(tick[j])
        tick.pop(j)
        n -= 1



