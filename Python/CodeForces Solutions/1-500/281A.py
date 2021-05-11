s = input()
l = list(s)
if not((ord(l[0])>=65) and (ord(l[0])<=90)):
    l[0] = chr(ord(l[0])-32)
print(*l, sep="")