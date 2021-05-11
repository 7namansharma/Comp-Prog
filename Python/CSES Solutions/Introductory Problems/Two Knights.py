n = int(input())
c = 24
if n==1:
    print("0")
elif n==2:
    print("0")
    print("6")
elif n==3:
    print("0")
    print("6")
    print("28")
else:
    print("0")
    print("6")
    print("28")
    for i in range(4, n+1):
        x = 4 * ((i*i) - (3*i) - 4)
        ans = (((i*i) * ((i*i)-1))/2) - (x + c)
        print(int(ans))

