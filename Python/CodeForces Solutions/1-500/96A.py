s = input()
c = 1
curr = s[0]
flag = False
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        c += 1
    else:
        c = 1
        curr = s[i+1]
    if c == 7:
        flag = True
        break
if flag:
    print("YES")
else:
    print("NO")

