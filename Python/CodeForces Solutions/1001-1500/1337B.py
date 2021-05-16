for i in range(int(input())):
    h, n, m = map(int, input().split())
    flag = False
    while n != 0 or m != 0:
        if n > 0 and m > 0:
            if h > 20 :
                n -= 1
                h = h//2 + 10
            else:
                m -= 1
                h -= 10
        elif n > 0 and m == 0:
            n -= 1
            h = h//2 + 10
        else:
            m -= 1
            h = h - 10
        #print(h)
        if h <= 0:
            print("YES")
            flag = True
            break
    if not flag:
        print("NO")

