n, m, a = map(int, input().split())
if n == m == a:
    print(1)
else:
    if n % a == 0 and m % a == 0:
        print(n//a * m//a)
    elif n % a != 0 and m % a == 0:
        print((n//a + 1) * m//a)
    elif n % a == 0 and m % a != 0:
        print(n//a * (m//a + 1))
    else:
        print((n // a + 1) * (m // a + 1))
