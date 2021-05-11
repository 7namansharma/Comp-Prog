n = int(input())
give = list(map(int, input().split()))
take = [0]*n
for i in range(n):
    take[i] = give.index(i+1) + 1
print(*take, sep = " ")