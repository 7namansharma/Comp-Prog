#BatStanRMAMJ
#1511B
l = [[0, 0], [2,  3], [11, 13], [101, 103], [1009, 1013], [10007, 10009], [100003, 100019], [1000003, 1000033], [10000019, 10000169], [100000007, 100000049]]
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    gcd = l[c][0]
    if a==b:
        x_factor = l[a-c+1][0]
        y_factor = l[b-c+1][1]
    else:
        x_factor = l[a-c+1][0]
        y_factor = l[b-c+1][0]
    x = gcd * x_factor
    y = gcd * y_factor
    print(x, y)

