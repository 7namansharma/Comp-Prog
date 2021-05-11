l = list(input())
l.sort()
flag = False
if(len(l)%2) == 0:
    dic = dict.fromkeys(l, 0)
    for i in l:
        dic[i] += 1
    for i in dic:
        if((dic[i]%2)!=0):
            print("NO SOLUTION")
            flag = True
            break
        else:
            dic[i] //= 2
    if(flag!=True):
        s = ""
        for i in dic:
            s+= i * dic[i]
        print(s+s[::-1])
else:
    dic = dict.fromkeys(l, 0)
    c1 = 0
    c2 = ""
    for i in l:
        dic[i] += 1
    for i in dic:
        if ((dic[i] % 2) == 0):
            c1 += 1
        else:
            c2 = i
    if (c1 != (len(set(l))-1)):
        print("NO SOLUTION")
    else:
        s = ""
        for i in dic:
            if ((dic[i] % 2) == 0):
                dic[i] //= 2
                s += i * dic[i]
        print(s + (c2 * dic[c2]) + s[::-1])


