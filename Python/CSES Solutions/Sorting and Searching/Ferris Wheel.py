n, x = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
i = 0
j = len(p) - 1
count = 0
countc = 0
while i<j and j != 0:
    #print(i, j)
    if p[j] <= x - p[i]:
        i += 1
        j -= 1
        count += 1
        countc += 2
    else:
        j -= 1
count += n - countc
print(count)
