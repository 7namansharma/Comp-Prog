n = int(input())
if ((n*(n+1))/2)%2!=0:
    print("NO")
else:
    print("YES")
    l_even1 = [1, 4]
    l_even2 = [2, 3]
    l_odd1 = [1, 2]
    l_odd2 = [3]
    if n%2==0:
        for i in range(5, n+1, 4):
            l_even1.append(i)
            l_even2.append(i + 1)
            l_even2.append(i + 2)
            l_even1.append(i + 3)
        print(len(l_even1))
        print(*l_even1, sep=" ")
        print(len(l_even2))
        print(*l_even2, sep=" ")
    else:
        for i in range(4, n, 4):
            l_odd1.append(i)
            l_odd2.append(i + 1)
            l_odd2.append(i + 2)
            l_odd1.append(i + 3)
        print(len(l_odd1))
        print(*l_odd1, sep=" ")
        print(len(l_odd2))
        print(*l_odd2, sep=" ")


