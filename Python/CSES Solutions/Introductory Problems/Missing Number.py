n = int(input())
l = list(map(int, input().split()))
l.sort()
flag = False
i = 1
while flag == False:
    if i!=l[i-1]:
        print(i)
        flag = True
        break
    i += 1
    if i == n:
        print(n)
        flag = True