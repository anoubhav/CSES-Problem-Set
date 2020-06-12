n = int(input())
ans = [n]
while n!=1:
    if n%2==0:
        n >>= 1
    elif n%2==1:
        n *= 3
        n += 1
    ans.append(n)
print(*ans)
