n, t = map(int, input().split())
l = []
l = list(map(int, input().split()))
pos = 1
i=0
flag = False
while(1):
    if pos == t:
        print("YES")
        flag = True
        break
    if pos<t:
        pos += l[i]
        i += l[i]
    else:
        break
    #print(pos)
if flag==False:
    print("NO")

