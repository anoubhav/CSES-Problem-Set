n = int(input())
nums = list(map(int, input().split()))
print((n*(n+1))//2 - sum(nums))