for _ in range(int(input())):
    a, b = map(int, input().split())
    n = a+b
    l = list(input())
    p_count = 0
    mid = False
    flag = False
    if n == 1:
        if l[0] == "?":
            mid = True
        else:
            if l[0] == "0" and a == 1:
                print("0")    
            elif l[0] == "1" and b == 1:
                print("1")
            else:
                print("-1")
            continue            
    if n%2!=0 and n!=1: 
        if l[(n//2)] == "0":
            a -= 1
        elif l[(n//2)] == "1":
            b -= 1
        else:
            mid = True
    for i in range(n//2):
        if l[i] == "0" == l[n-i-1]:
            a -= 2
        elif l[i] == "1" == l[n-i-1]:
            b -= 2
        elif l[i] == "?" == l[n-i-1]:
            p_count += 1
        elif (l[i] == "0" and l[n-i-1] =="?") or (l[i] == "?" and l[n-i-1] =="0"):
            a -= 2
            if l[i] == "0" and l[n-i-1] =="?":
                l[n-i-1] = "0"
            else:
                l[i] = "0"
        elif (l[i] == "1" and l[n-i-1] =="?") or (l[i] == "?" and l[n-i-1] =="1"):
            b -= 2
            if l[i] == "1" and l[n-i-1] =="?":
                l[n-i-1] = "1"
            else:
                l[i] = "1"
        else:
            print("-1")
            flag = True
            break
        if a<0 or b<0:
            print("-1")
            flag = True 
            break
    #print(p_count)
    if flag == False:
        if ((a//2)+(b//2)) == p_count:
            #print(a, b)
            for i in range(n//2):
                if l[i] == "?" == l[n-i-1]:
                    if a >= 2:
                        l[i] = "0"
                        l[n-i-1] = "0"
                        a -= 2
                    else:
                        l[i] = "1"
                        l[n-i-1] = "1"
                        b -= 2
        else:
            print("-1")
            continue
        if mid == True:
            if a!=0:
                l[(n//2)] = "0"
            else:
                l[(n//2)] = "1"
        print(*l, sep = "")
