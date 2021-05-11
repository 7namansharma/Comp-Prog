for _ in range(int(input())):
    n, k = map(int, input().split())
    if ((n-1)//2) < k:
        print("-1")
    else:
        l = [i+1 for i in range(n)]
        count = 0
        for i in range(1, n, 2):
            if count < k:
                 temp = l[i]
                 l[i] = l[i+1]
                 l[i+1] = temp
                 count += 1
        print(*l, sep = " ")