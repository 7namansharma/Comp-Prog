n1 = input()
n2 = input()
length = len(n1)
n3 = bin(int(n1, 2) ^ int(n2, 2))[2:]
n3_string = str(n3)
if len(n3_string) < length:
    print("0"*(length-len(n3_string)), sep="", end="")
print(n3)

