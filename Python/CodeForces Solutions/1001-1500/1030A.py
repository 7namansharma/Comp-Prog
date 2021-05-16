n = int(input())
l = list(map(int, input().split()))
if (l[0] == 0) and len(set(l)) == 1:
    print("EASY")
else:
    print("HARD")
