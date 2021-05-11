mod = 1000000007
for _ in range(int(input())):
    n, k = map(int, input().split())
    print(n**k%mod)