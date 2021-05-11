n = int(input())
l = []
if n==2 or n==3:
    print("NO SOLUTION")
elif n==1:
    print("1")
elif n==4:
    print("2 4 1 3")
else:
    if n%2 == 0:
        for i in range(n, 0, -2):
            l.append(i)
        for i in range(n-1, -1, -2):
            l.append(i)
    else:
        for i in range(n, -1, -2):
            l.append(i)
        for i in range(n-1, 0, -2):
            l.append(i)
print(*l, sep = " ")