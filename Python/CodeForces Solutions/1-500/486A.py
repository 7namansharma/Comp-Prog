n = int(input())
sum = 0
if n % 2 != 0:
    sum = (((n+1)//2)*((n+1)//2)) - (((n-1)//2)*(((n-1)//2) + 1))
else:
    sum = ((n//2)*(n//2)) - ((n//2)*((n//2)+1))
print(int(-sum))