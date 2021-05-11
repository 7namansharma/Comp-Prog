mat = [[0]for i in range(5)]
reqi = 0
reqj = 0
for i in range(5):
    mat[i] = list(map(int, input().split()))
for i in range(5):
    for j in range(5):
        if mat[i][j] == 1:
            reqi = i
            reqj = j
print((abs(reqi-2)+abs(reqj-2)))