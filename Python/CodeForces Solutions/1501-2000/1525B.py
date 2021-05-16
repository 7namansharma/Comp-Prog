for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    if l==sorted(l):
        print("0")
        continue
    if l[0]==1 or l[n-1]==n:
        print("1")
        continue
    if l[0]==n:
        if l[n-1]==1:
            print("3")
        else:
            print("2")
        continue
    else:
        print("2")
