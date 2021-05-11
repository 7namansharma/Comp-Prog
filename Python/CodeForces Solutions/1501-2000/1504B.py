for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    flag = False
    if a == b:
        print("YES")
        continue
    if n%2!=0:
        if a[n-1]!=b[n-1]:
            print("NO")
            continue
        else:
            a = a[:n-1]
            b = b[:n-1]
            n = n - 1
    for i in range(n-1, -1, -2):
        if a[i]!=b[i] and a[i-1]!=b[i-1]:
            a = a[:i+1]
            b = b[:i+1]
            a_l = list(a)
            if a.count('1') == b.count('1'):
                for j in range(i+1):
                    if a_l[j] == '1':
                        a_l[j] = '0'
                    else:
                        a_l[j] = '1'
            else:
                print("NO")
                flag = True
                break
            a = ""
            a = (a.join(a_l))
            #print(a)
        elif (a[i]!=b[i] and a[i-1]==b[i-1]) or (a[i]==b[i] and a[i-1]!=b[i-1]):
            print("NO")
            flag = True
            break
        else:
            pass
    if flag == False:
        print("YES")
