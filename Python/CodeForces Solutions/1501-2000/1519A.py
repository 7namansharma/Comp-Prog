for _ in range(int(input())):
    r, b, d = map(int, input().split())
    if r==0 or b==0:
        print("NO")
        continue
    mini = min(r, b)
    maxi = max(r, b)
    if mini*(d+1)>=maxi:
        print("YES")
    else:
        print("NO")
        