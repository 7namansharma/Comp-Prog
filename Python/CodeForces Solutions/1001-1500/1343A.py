for i in range(int(input())):
    n = int(input())
    twopower = 1
    suma = 1
    flag = False
    while not flag:
        twopower *= 2
        suma += twopower
        if n % suma == 0:
            print(n//suma)
            flag = True
