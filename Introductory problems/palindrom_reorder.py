from collections import Counter
from sys import stdin
s = stdin.readline().strip()
n = len(s)

c = Counter(s)
ans = ''
oddset = set()
oddv = ''
for k, v in c.items():
    if v%2 == 1:
        oddset.add(k)
        oddv = k
        if n%2 == 0 or len(oddset)>1:
            print('NO SOLUTION')
            exit()
    else:

        ans = k*(v//2) + ans + k*(v//2)

# if odd frequency character exists, add to the center of existing string.
if len(oddset) == 1:
    l = len(ans)
    ans = ans[:l//2] + oddv*c[oddv] + ans[l//2:]

print(ans)
            
    

