for _ in range(int(input())):
    px, py = map(int, input().split())
    s = input()
    x, y = 0, 0
    res = ''
    di = {"U": 0, "D": 0, "L": 0, "R": 0}
    u, d, l, r = 0, 0, 0, 0
    for i in s:
        di[i]+=1
    f, f1 = False, False
    if px>=x:
        if di["R"]>=px:
            f = True
    elif px<x:
        if di["L"]>=abs(px):
            f = True
    if py>=y:
        if di["U"]>=py:
            f1 = True
    else:
        if di["D"]>=abs(py):
            f1 = True
    if f and f1:
        print("YES")
    else:
        print("NO")

