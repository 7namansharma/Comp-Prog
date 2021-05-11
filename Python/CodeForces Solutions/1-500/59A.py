s = input()
l = list(s)
cu = 0
cl = 0
for i in range(len(l)):
    if 65 <= ord(l[i]) <= 90:
        cu += 1
    else:
        cl += 1
if cu > cl:
    print(s.upper())
else:
    print(s.lower())
