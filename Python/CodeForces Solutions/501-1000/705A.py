n = int(input())
for i in range(1, n+1):
    if i != n:
        if i % 2 != 0:
            print("I hate that", end=" ")
        else:
            print("I love that", end=" ")
    else:
        if i % 2 != 0:
            print("I hate it", end=" ")
        else:
            print("I love it", end=" ")