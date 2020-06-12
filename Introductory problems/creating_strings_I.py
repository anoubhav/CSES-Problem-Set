import itertools as it
from math import factorial
from collections import Counter
s = input()
n = len(s)

# Number of permutations with repetitions
c = Counter(s)
ans = factorial(n)
for k, v in c.items():
    ans //= factorial(v)
print(ans)

## Using itertools
def inbuilt(s, n):
    seen = set()
    for string in it.permutations(sorted(s)):
        t = ''.join(string)
        if t not in seen:
            seen.add(t)
            print(t)  

## Using recursion: permutation without any duplicates. To avoid duplicates we use set.
def recursion_no_dup(s, n):
    rep = set() # checks repeats
    lst = list() # stores answer

    def recurse(s, pos, n):
        if pos == n-1:
            st = ''.join(s)
            if st not in rep:
                rep.add(st) 
                lst.append(st)
            return
        else:
            s = s.copy()
            for i in range(pos, n):
                s[i], s[pos] = s[pos], s[i]
                recurse(s, pos + 1, n)

    # to ensure alphabetic order
    recurse(sorted(list(s)), 0 , n) 
    print(*lst, sep='\n')


def recursion_with_dup(s, n):
    def valid_swap(s, start, i):
        for ind in range(start, i):
            if s[ind] == s[i]:
                return False
        return True
    
    def recurse(s, pos, n):
        if pos == n-1:
            ans.append(''.join(s))
        else:
            for i in range(pos, n):
                if valid_swap(s, pos, i):
                    s[pos], s[i] = s[i], s[pos]
                    recurse(s, pos + 1, n)
                    s[pos], s[i] = s[i], s[pos]
    
    ans = []
    recurse(sorted(list(s)), 0, n)
    print(*sorted(ans), sep = '\n')

recursion_with_dup(s, n)
# recursion_no_dup(s, n)
# inbuilt(s, n)