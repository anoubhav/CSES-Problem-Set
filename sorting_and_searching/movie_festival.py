from sys import stdin
n = int(input())
lst = []
for _ in range(n):
    s, e = map(int, stdin.readline().split())
    lst.append((s, e))
    
lst.sort(key = lambda x: x[1])

prev = lst[0]
ans = 1

for tup in lst[1:]:
    if tup[0] < prev[1]:
        continue
    else:
        ans += 1
        prev = tup

print(ans)