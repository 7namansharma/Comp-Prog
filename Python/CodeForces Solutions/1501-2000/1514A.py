from math import sqrt
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    flag = False
    for i in l:
        if sqrt(i) != int(sqrt(i)):
            print("YES")
            flag = True
            break
    if flag == False:
        print("NO")