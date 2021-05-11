l = list(input())
count = 1
max = 1
for i in range(1, len(l)):
    if l[i]==l[i-1]:
        count += 1
        if max<count:
            max = count
    else:
        count = 1
print(max)