n = int(input())
l = list(map(int, input().split()))
c1 = 0
c2 = 0
c3 = 0
cabs = 0
for i in l:
    if i == 1:
        c1 += 1
    elif i == 2:
        c2 += 1
    elif i == 3:
        c3 += 1
    else:
        cabs += 1
#print(c1, c2, c3, cabs)
mini = min(c3, c1)
cabs += mini
c3 -= mini
c1 -= mini
cabs += c2//2
c2 %= 2
if c1 != 0 and c2 != 0:
    c1 -= 2
    c2 = 0
    cabs += 1
#print(c1, c2, c3, cabs)
if c1 > 0:
    if c1 % 4 == 0:
        cabs += c1//4
    else:
        cabs += c1//4 + 1
#print(c1, c2, c3, cabs)
if c2 != 0:
    cabs += 1
    c2 = 0
if c3 != 0:
    cabs += c3
#print(c1, c2, c3, cabs)
print(cabs)
