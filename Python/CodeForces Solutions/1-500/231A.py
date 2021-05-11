cou = 0
for _ in range(int(input())):
    l = list(map(int, input().split()))
    c = l.count(1)
    if c >= 2:
        cou += 1
    c = 0
print(cou)
