n, x = map(int, input().split())
nums = list(map(int, input().split()))


def using_dict(n, x, nums):
    # O(N) time complexity and space complexity
    from collections import defaultdict as dd
    d = dd(list)

    for i in range(n):
        d[nums[i]].append(i)

    ans = (-1, -1)
    for k in d.keys():
        if x-k in d:
            if x - k == k:
                if len(d[k]) > 1:
                    ans = (d[k][0] + 1, d[k][1] + 1)
                    break
            else:
                ans = (d[k][0] + 1, d[x-k][0] + 1)
                break

    if ans == (-1, -1):
        print('IMPOSSIBLE')
    else:
        print(*ans)

def two_pointer(n, x, arr):
    # O(nlogn) time complexity and O(n) space
    nums = arr.copy()
    nums.sort()
    l, r = 0, n-1
    ans = (-1, -1)
    while l<r:
        if nums[l] + nums[r] == x:
            ans = (nums[l], nums[r])
            break
        elif nums[l] + nums[r] > x:
            r -= 1
        else:
            l += 1

    if ans == (-1, -1): 
        print('IMPOSSIBLE')
    else:
        fl, fr = 0, 0
        soln = [0, 0]
        # find the indices
        for i, num in enumerate(arr):
            if num == ans[0] and not fl:
                fl = 1
                soln[0] = i+1
            elif num == ans[1] and not fr:
                fr = 1
                soln[1] = i+1
            elif fr and fl: break
        soln.sort()
        print(*soln)

two_pointer(n, x, nums)