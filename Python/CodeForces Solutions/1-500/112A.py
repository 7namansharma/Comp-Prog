a1 = input()
a2 = input()
a1 = a1.upper()
a2 = a2.upper()
flag = 0
if a1 == a2:
    print(0)
else:
    for _ in range(len(a1)):
        if ord(a1[_]) < ord(a2[_]):
            flag = -1
            break
        elif ord(a1[_]) > ord(a2[_]):
            flag = 1
            break
    print(flag)