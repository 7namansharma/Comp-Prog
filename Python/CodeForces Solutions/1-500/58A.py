s = input()
x = s.find("h")
y = s.find("e", x+1)
z = s.find("l", y+1)
a = s.find("l", z+1)
b = s.find("o", a+1)
if (x!=-1 and y!=-1 and z!=-1 and a!=-1 and b!=-1):
    print("YES")
else:
    print("NO")

    