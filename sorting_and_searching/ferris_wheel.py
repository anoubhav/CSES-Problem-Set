from collections import deque
n, x = map(int, input().split())
weights = list(map(int, input().split()))

def using_deque(n, x, weights):

    weights.sort()

    weights = deque(weights)
    ans = 0
    while len(weights)>1:
        if weights[-1] + weights[0] > x:
            weights.pop()
            ans += 1
        else:
            weights.pop()
            weights.popleft()
            ans += 1

    if len(weights):
        ans += 1
    print(ans)

def using_two_pointers(n, x, weights):
    weights.sort()
    l, r = 0, n-1
    ans = 0
    while l<=r:
        if weights[l] + weights[r] > x:
            r -= 1
        else:
            l += 1
            r -= 1
        ans += 1 

    print(ans)

using_two_pointers(n, x, weights)