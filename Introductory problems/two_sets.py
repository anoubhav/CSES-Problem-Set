n = int(input())
t = (n*(n+1))//2
if t%2 == 1:
    print('NO')
else:
    s = t//2
    s1, s2 = [], []
    if n%2 == 1:
        s1 += [1, 2]
        s2 = [3]

    parity = 0
    for i in range(4 if n%2 else 1, n+1, 2):
        if parity == 0:
            s1.append(i)
            s2.append(i+1)
        elif parity == 1:
            s1.append(i+1)
            s2.append(i)
        parity = (parity + 1)%2
    
    if parity == 1:
        print('NO')
    else:
        print('YES')
        print(len(s1))
        print(*s1)
        print(len(s2))
        print(*s2)

    

