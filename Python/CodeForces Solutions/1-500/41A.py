s1 = input()
s2 = input()
s1 = "".join(reversed(s1))
if s2 == s1:
    print("YES")
else:
    print("NO")
