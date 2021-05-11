for i in range(int(input())):
    sum = 0
    y, x = map(int, input().split())
    n = max(x,y)
    sum += (n-1) * (n-1)
    if n%2!=0:
        sum += x + (n-y)
    else:
        sum += y + (n-x)
    print(sum)

