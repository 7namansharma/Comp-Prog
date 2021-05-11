for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    flag = False
    for i in range(1, n-1):
        if l[i]!=l[i-1] and l[i]!=l[i+1]:
            print(i+1)
            flag = True
            break
    if flag==False:
        if l[1]!=l[0]:
            print("1")
        else:
            print(n)
            