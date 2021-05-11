n, t = map(int, input().split())
s = input()
l = list(s)
for i in range(t):
    j = 0
    while j < n-1:
        if l[j] == 'B' and l[j+1] == 'G':
            l[j+1] = "B"
            l[j] = "G"
            j += 1
        j += 1
print(*l, sep="")