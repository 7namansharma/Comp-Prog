n = input()
l = list(map(int, input().split()))
l.sort(reverse=True)
sumall = sum(l)
sum = 0
c = 0
for i in l:
    if sum > (sumall-sum):
        break
    sum += i
    c += 1
print(c)

