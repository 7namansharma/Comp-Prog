n, m = map(int, input().split())
day = 0
socks = n
while socks != 0:
    socks -= 1
    day += 1
    if day % m == 0:
        socks += 1
print(day)