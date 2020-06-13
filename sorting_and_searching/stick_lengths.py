from sys import stdin
n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))

nums.sort()
med = nums[n//2]
ans = 0
for num in nums:
    ans += abs(med - num)
print(ans)