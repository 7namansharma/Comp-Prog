for _ in range(int(input())):
    n = int(input())
    s = input()
    l = list(s)
    t_count = 0
    m_count = 0
    flag = True
    if l.count("T") != 2 * l.count("M"):
        print("NO")
        continue
    for i in l:
        if i == "T":
            t_count += 1
        else:
            m_count += 1
        if m_count > t_count:
            print("NO")
            flag = False
            break
    t_count = 0
    m_count = 0
    if flag == True:
        for i in range(n-1, -1, -1):
            if l[i] == "T":
                t_count += 1
            else:
                m_count += 1
            if m_count > t_count:
                print("NO")
                flag = False
                break
    if flag == True:
        print("YES")







