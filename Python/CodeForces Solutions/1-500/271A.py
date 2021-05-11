n = int(input())
for i in range(n+1, 9013):
    x = i
    l = []
    while x != 0:
        l.append(x % 10)
        x = x // 10
    if len(set(l)) == 4:
        print(i)
        break
