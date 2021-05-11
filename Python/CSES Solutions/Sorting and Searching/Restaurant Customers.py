dic = dict.fromkeys(list(range(1000000000)), 0)
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    for j in range(a, b):
        dic[j] += 1
print(max(dic.values()))
