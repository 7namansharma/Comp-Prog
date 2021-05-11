for _ in range(int(input())):
    n = int(input())
    l = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        l[i] = list(input())
    x1, x2, y1, y2 = 0, 0, 0, 0
    count = 0
    for i in range(n):
        for j in range(n):
            if l[i][j] == '*':
                if count == 0:
                    x1 = i
                    y1 = j
                    count += 1
                else:
                    x2 = i
                    y2 = j
    if x1 == x2:
        if n%2!=0 and (2*x1)==n-1:
            l[n-x1][y2] = '*'
            l[n-x2][y1] = '*'
        else:
            l[n-x1-1][y2] = '*'
            l[n-x2-1][y1] = '*'
    elif y1 == y2:
        if n%2!=0 and (2*y1)==n-1:
            l[x1][n-y2] = '*'
            l[x2][n-y1] = '*'
        else:
            l[x1][n-y2-1] = '*'
            l[x2][n-y1-1] = '*'
    else:
        l[x1][y2] = '*'
        l[x2][y1] = '*'
    for i in range(n):
        for j in range(n):
            print(l[i][j], sep ="", end="")
        print("")


