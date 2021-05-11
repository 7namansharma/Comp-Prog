c = 1
for i in range(int(input())):
    if i == 0:
        n = int(input())
        curr = n
    else:
        n = int(input())
    if curr != n:
        c += 1
        curr = n
print(c)
