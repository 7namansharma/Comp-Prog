a, b = map(int, input().split())
c = 1
ratio = 1.5
while (b/a) >= ratio:
    ratio = 1.5 * ratio
    c += 1
print(c)