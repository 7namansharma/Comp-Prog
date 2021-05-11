for _ in range(int(input())):
    n = int(input())
    s = input()
    if '.' not in s:
        print("0")
        continue
    if '*' not in s: 
        print("0")
        continue
    if s.count('*')==1:
        print("0")
        continue
    count = s.count('*')
    if count%2==0:
        mid = count//2
    else:
        mid = (count//2) + 1
    mid_pos = 0
    count_star = 0 
    for i in range(n):
        if s[i]=="*":
            count_star += 1
        if count_star == mid:
            mid_pos = i
            break
    ans = 0
    #print(mid_pos)
    for i in range(n):
        if s[i]=='*':
            ans += abs(i-mid_pos)
    #print(ans)
    if count%2!=0:
        ans -= (mid-1)*mid
    else:
        ans -= ((mid-1)*mid)//2 + (mid*(mid+1))//2
    print(ans)