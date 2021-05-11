for _ in range(int(input())):
    s = input()
    l = list(s)
    flag = False
    for i in range(len(l)):
        if l[i]!='a':
            l.insert(len(l)-i, 'a')
            flag = True
            print("YES")
            print(*l, sep="")
            break
    if flag==False:
        print("NO")
