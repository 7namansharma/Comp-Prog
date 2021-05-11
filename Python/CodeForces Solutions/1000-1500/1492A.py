for _ in range(int(input())):
    p, a, b, c = map(int, input().split())
    if p % a == 0:
        a_come = (p//a) * a
    else:
        a_come = ((p//a) + 1) * a
    if p % b == 0:
        b_come = (p//b) * b
    else:
        b_come = ((p//b) + 1) * b
    if p % c == 0:
        c_come = (p // c) * c
    else:
        c_come = ((p // c) + 1) * c
    ans = min(a_come, b_come, c_come)
    print(ans-p)



