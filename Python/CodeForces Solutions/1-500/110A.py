n = int(input())
c = 0
while n != 0:
    if (n % 10 == 4) or (n % 10 == 7):
        c += 1
    n = n // 10
if c==0:
    print("NO")
else:
    flag = False
    while c != 0:
        if (c % 10 != 4) and (c % 10 != 7):
            flag = True
            break
        c = c // 10
    if flag == True:
        print("NO")
    else:
        print("YES")


