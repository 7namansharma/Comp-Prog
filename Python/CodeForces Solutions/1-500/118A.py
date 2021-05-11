s = input()
l = list(s)
L = ["A", "O", "Y", "E", "U", "I", "a", "e", "i", "o", "u", "y"]
i = 0
n = len(l)
while i < n:
    if l[i] in L:
        l.remove(l[i])
        i -= 1
        n -= 1
    i += 1
    #print(i)
    #print(l)
    #print(n)
n = len(l)
for i in range(n):
    #print(ord(i))
    if 65 <= ord(l[i]) <= 90:
        #print(chr(ord(i)+32))
        l[i] = chr(ord(l[i])+32)
#print(l)
print(".", sep="", end="")
print(*l, sep=".", end="")


