k, n, w = map(int, input().split())
req = ((w*(w+1))/2) * k
if req > n:
    print(int(req - n))
else:
    print(0)