n = int(input())
weights = list(map(int, input().split()))

totsum = sum(weights)

def recursion_exponential(weights, i, currsum, totsum):
    if i == 0:
        return abs((totsum - currsum) - currsum)
    else:
        return min(recursion_exponential(weights, i-1, currsum + weights[i], totsum), recursion_exponential(weights, i-1, currsum, totsum))
print(recursion_exponential(weights, n-1, 0, totsum))

def inbuilt_exponential(weights, n, half):
    # O(2*len(weights))
    minsf = 10**9
    ans = 0
    import itertools as it
    for mask in it.product([1, 0], repeat = len(weights)):
        s1 = sum([weights[i] for i in range(n) if mask[i]])
        if abs(half - s1) < minsf:
            minsf = abs(half - s1)
            ans = 2*abs(half - s1)
    print(int(ans))
