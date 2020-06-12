n = int(input())
num = list(map(int, input().split()))

# print(len(set(num)))

num.sort()
ans = 0
for i in range(1, n):
    if num[i]!=num[i-1]:
        ans += 1
print(ans + 1)