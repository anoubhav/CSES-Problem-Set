n, m, k = map(int, input().split())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))

alist.sort()
blist.sort()

ind1, ind2 = 0, 0
ans = 0
while ind1 < len(alist) and ind2 < len(blist):
    if alist[ind1] - k <= blist[ind2] <= alist[ind1] + k:
        ans += 1
        ind1 += 1
        ind2 += 1
    elif blist[ind2] > alist[ind1] + k:
        ind1 += 1
    else:
        ind2 += 1
print(ans)