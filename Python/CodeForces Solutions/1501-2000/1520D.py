for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    diff = []
    for i in range(n):
        diff.append(l[i]-(i+1))
    diff.sort()
    #print(diff)
    count = 0
    curr = diff[0]
    suma = 0
    for i in range(n):
        if diff[i] == curr:
            count += 1
        else:
            suma += (count * (count-1))//2
            curr = diff[i]
            count = 1
        if i==n-1:
            suma += (count * (count-1))//2
    print(suma)