import math
for _ in range(int(input())):
    k = int(input())
    hcf = math.gcd(100, k)
    ans = k//hcf + (100-k)//hcf
    print(ans)    