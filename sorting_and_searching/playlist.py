from sys import stdin
n = int(stdin.readline())
lst = list(map(int, stdin.readline().split()))

last_seen_ind = dict()
msf = 1
start = 0

for end, num in enumerate(lst):
    if num in last_seen_ind:
        msf = max(msf, end - start)
        for i in range(start, last_seen_ind[num]):
            del last_seen_ind[lst[i]]

        start = last_seen_ind[num] + 1
        last_seen_ind[num] = end
    else:
        last_seen_ind[num] = end
msf = max(msf, end - start + 1)
print(msf)

