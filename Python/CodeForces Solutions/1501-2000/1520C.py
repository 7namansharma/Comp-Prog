for _ in range(int(input())):
    n = int(input())
    l = []
    if n==1:
        print("1")
        continue
    if n==2:
        print("-1")
        continue
    for i in range(1, (n*n)+1):
        if i%2!=0:
            l.append(i)
    for i in range(1, (n*n)+1):
        if i%2==0:
            l.append(i)
    for i in range(n):
        for j in range(n):
            print(l[n*i + j], end = " ")
        print("\n")  