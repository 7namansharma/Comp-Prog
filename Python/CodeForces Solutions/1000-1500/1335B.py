for _ in range(int(input())):
    n, a, b = map(int, input().split())
    c = 97
    l = []
    for i in range(n):
        if c == (97 + b):
            c = 97
        l.append(chr(c))
        c += 1
    print(*l, sep="")