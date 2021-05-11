n = int(input())
if n >= 0:
    print(n)
else:
    num1 = -(abs(n)//10)
    num2 = -(((abs(n)//100) * 10) + (abs(n) % 10))
    if num1 > num2:
        print(num1)
    else:
        print(num2)