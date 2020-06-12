string = input()
msf, ans = 0, 1
prev =  string[0]

for i, char in enumerate(string):
    if char==prev:
        msf += 1
    else:
        prev = char
        ans = max(msf, ans)
        msf = 1

ans = max(msf, ans)
print(ans)
