n = int(input())
s = input()
l = list(s)
c0 = 0
c1 = 0
for i in l:
    if i == '0':
        c0 += 1
    else:
        c1 += 1
#print(l, c1, c0)
print(abs(c1-c0))

