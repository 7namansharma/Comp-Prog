for _ in range(int(input())):
    n = int(input())
    if n%2050==0:
        suma = 0 
        n = n//2050
        while(n!=0):
            suma += n % 10
            n = n//10
        print(suma)
    else:
        print(-1)