from sys import stdin
n = int(stdin.readline())
lst = list(map(int, stdin.readline().split()))

def binary_insertion(tops, cube):
    def binsert(tops, cube):
        lo, hi = 0, len(tops)-1
        ans = -1
        while lo<=hi:
            mid = lo + (hi - lo)//2
            if cube < tops[mid]:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        if ans == -1:
            tops.append(cube)
        else:
            tops[ans] = cube

    tops = [lst[0]] # tops of the towers
    for cube in lst[1:]:
        binsert(tops, cube)
    print(len(tops))

def inbuilt(tops, cube):
    from bisect import bisect_right
    top=[lst[0]]
    for i in lst[1:]:
        j=bisect_right(top,i)
        if j<len(top):
            top[j]=i
        else:
            top.append(i)
    print(len(top))