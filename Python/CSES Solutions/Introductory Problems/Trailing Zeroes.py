n = int(input())
sum = 0
i = 1
while ((pow(5, i))<=n):
    sum += (n//(pow(5, i)))
    i += 1
print(int(sum))