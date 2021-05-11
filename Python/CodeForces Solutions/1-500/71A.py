for i in range(int(input())):
    n = input()
    if len(n)>10:
        print(n[0], len(n)-2, n[-1], sep="")
    else:
        print(n)
