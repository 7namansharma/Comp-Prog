for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l_even = []
    l_odd = []
    for i in l:
        if i%2 == 0:
            l_even.append(i)
        else: 
            l_odd.append(i)
    l = l_even + l_odd
    print(*l, sep = " ")