bus = 0
minbus = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    bus = bus + (b-a)
    minbus = max(minbus, bus)
print(minbus)