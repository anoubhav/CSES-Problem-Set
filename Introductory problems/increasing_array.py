n = int(input())
nums = list(map(int, input().split()))

ans = 0
for i in range(1, len(nums)):
    if nums[i-1] - nums[i] > 0:
        ans += nums[i-1] - nums[i]
        nums[i] = nums[i-1]
print(ans)