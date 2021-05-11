#BatStanRMAMJ
#1511A
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    up = 0
    for i in l:
        if i == 1 or i == 3:
            up += 1
    print(up) 