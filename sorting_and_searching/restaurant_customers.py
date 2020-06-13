from sys import stdin
n = int(input())
lst = []
for _ in range(n):
    a, l = map(int, stdin.readline().split())
    lst.append((a, 'a'))
    lst.append((l, 'l'))

ans, ssf = 0, 0
for tup in sorted(lst, key = lambda x: x[0]):
    ssf += (1 if tup[1] == 'a' else -1)
    ans = max(ans, ssf)
print(ans)