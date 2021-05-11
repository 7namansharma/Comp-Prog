s = input()
l = list(s)
i = 0
while i < len(l)-2:
    if l[i] == 'W' and l[i+1] == 'U' and l[i+2] == 'B':
        l.pop(i)
        l.pop(i)
        l.pop(i)
        if i != 0 and l[i-1] != " ":
            l.insert(i, " ")
            i -= 1
    else:
        i += 1
print(*l, sep="")