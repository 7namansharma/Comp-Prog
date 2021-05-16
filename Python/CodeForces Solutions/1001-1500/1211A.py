n = int(input())
l = list(map(int, input().split()))
new = l
new = set(new)
new = sorted(new)
if len(new) <= 2:
    print("-1 -1 -1")
else:
    for i in range(3):
        for j in range(n):
            if new[i] == l[j]:
                print(j+1, end=" ")
                break
