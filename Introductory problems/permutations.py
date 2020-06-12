n = int(input())
if n == 1:
    print(1)
elif n in [2, 3]:
    print('NO SOLUTION')
else:
    if n%2 == 0:
        evens = list(range(2, n+1, 2))
        odds = list(range(1, n, 2))
    else:
        evens= list(range(2, n, 2))
        odds = list(range(1, n+1, 2))
    print(*(evens + odds))