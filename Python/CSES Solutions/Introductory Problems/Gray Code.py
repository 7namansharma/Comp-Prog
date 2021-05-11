n = int(input())
m = [[0 for i in range(n)] for j in range(2**n)]
k = 1
c0 = 0
c1 = 0
co = 0
for i in range(n-1, -1, -1):
    co = (2**(k-1))
    while co<(2**n):
        if ((c1<=(2**k)-1) and (c0 == 0)):
            m[co][i] = 1
            c1 += 1
        else:
            c1 = 0
            c0 += 1
            if (c0 == (2**k)):
                c0 = 0
        co += 1
    k += 1
    c1 = 0
    c0 = 0
for i in m:
    print(*i, sep='')
