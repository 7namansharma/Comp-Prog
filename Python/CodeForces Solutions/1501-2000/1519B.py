for _ in range(int(input())):
    n, m, k = map(int, input().split())
    req = 0
    req = 1*(m-1) + m*(n-1)
    if req == k:
        print("YES")
    else:
        print("NO")