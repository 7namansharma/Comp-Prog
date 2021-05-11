for _ in range(int(input())):
    n = int(input())
    s = input()
    count_prev = 0
    count = 0
    changes = 0
    for i in s:
        if i == "(":
            count -= 1
        else:
            count += 1
        if count>0 and count>count_prev:
            #print(i, count)
            changes += 1
            count_prev = count 
    print(changes)

            