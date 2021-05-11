import math
from itertools import permutations
l = list(input())
l.sort()
dic = dict.fromkeys(l, 0)
for i in l:
    dic[i] += 1
den = 1
for i in dic:
    den *= math.factorial(dic[i])
num = (math.factorial(len(l)))//den
print(num)
n = []
p = list(permutations(l))
p.sort()
for i in set(p):
    n.append(''.join(i))
n.sort()
for i in n:
    print(i)



