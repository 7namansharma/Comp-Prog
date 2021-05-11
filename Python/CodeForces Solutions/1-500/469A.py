n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
c = 0
p = l1[0]
q = l2[0]
for i in range(1, n+1):
    flag = False
    if i in l1[1:] or i in l2[1:]:
        flag = True
    if flag:
        c += 1
if c == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
