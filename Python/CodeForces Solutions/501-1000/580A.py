n = int(input())
l = list(map(int, input().split()))
k = 1
maxi = 0
for i in range(1, n):
    if l[i] >= l[i-1]:
        k += 1
    else:
        maxi = max(maxi, k)
        k = 1
print(max(maxi, k))