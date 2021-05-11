import math
for _ in range(int(input())):
    a, b = map(int, input().split())
    if b==1:
        print("NO")
        continue
    if b==2:
        print("YES")
        print(a*3, a*5, a*8)
        continue
    print("YES")
    print(a, a*(b-1), a*b)