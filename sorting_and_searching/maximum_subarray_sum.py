n = int(input())
lst = list(map(int, input().split()))

ans, msf = lst[0], lst[0]

for num in lst[1:]:
    msf = max(msf + num, num)
    ans = max(ans, msf)
print(ans)