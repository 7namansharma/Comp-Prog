for _ in range(int(input())):
    n = int(input())
    s = input()
    l = []
    a = []
    check = True
    l.append(s[0])
    for i in range(1, n):
        if s[i-1]!=s[i]:
            l.append(s[i])
    for i in l:
        a.append(l.count(i))
    for i in a:
        if i != 1:
            check = False
            break
    #print(l, a)
    if check:
        print("YES")
    else:
        print("NO")