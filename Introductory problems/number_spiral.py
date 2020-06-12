t = int(input())
for _ in range(t):
    r, c = map(int, input().split())

    mx = max(r, c)
    mi = min(r, c)
    if mx%2 == 0:
        lst = [(mx-1)**2 + 1, mx*mx]
        if mx == r:
            print(lst[1] - mi + 1)
        else:
            print(lst[0] + mi - 1)

        
    else:
        lst = [mx*mx, (mx-1)**2 + 1]
        if mx == r:
            print(lst[1] + mi - 1)
        else:
            print(lst[0] - mi + 1)
    
    