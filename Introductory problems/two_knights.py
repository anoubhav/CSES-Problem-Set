def isvalid(r, c, k):
    if 0<=r<=k-1 and 0<=c<=k-1:
        return True
    return False

import itertools as it
from fractions import Fraction
coords = list(it.product([-1, 1], [2, -2]))

# calling this function from 1-->10000 yields TLE
def numways_naive(k):
    t = k*k
    allways = (t*(t-1))//2
    poss = 0
    for r in range(k):
        for c in range(k):
            for move in coords:
                if isvalid(r + move[0], c + move[1], k):
                    poss += 1
                if isvalid(r + move[1], c + move[0], k):
                    poss += 1
            
    return (allways - poss//2)

# accepted
def numways_mine(k):
    t = k*k
    allways = (t*(t-1))//2
    poss = 0
    if k>=4:
        # 8 ways
        poss += 8*((k-4)**2)
        # 6 ways
        poss += 6*(4*(k - 4))
        # 4 ways
        poss += 4*(4 + 4*(k-4))
        # 3 ways
        poss += 3*8
        # 2 ways
        poss += 2*4

        return allways - poss//2


    else:
        return numways_naive(k)

# accepted
def numways_vegeta(i):
    # When two knights threaten each other they either form a 2x3 rectangle or a 3x2 rectangle. 
    # In ixi grid: There are (i-1)x(i-2) 2x3 rectangles . And (i-2)x(i-1) 3x2 rectangles. In 2x3 or 3x2 you can place knights in 2 valid pairs. answer: 2*(no. of 2x3) + 2(no. of 3x2) = 4x(i-1)x(i-2)
    t = k*k
    allways = (t*(t-1))//2
    return allways - 4*(i-1)*(i-2)




n = int(input())
solns = []
for k in range(1, n+1):
    # print(numways_mine(k))
    print(numways_vegeta(k))


## Checking the ratio of consecutive answers; no pattern
# for i in range(2, n):
#     print(solns[i]/solns[i-1])


