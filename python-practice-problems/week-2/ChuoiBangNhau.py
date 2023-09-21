def has_common_char(s1, s2):
    for c in s1:
        if c in s2:
            return True
    return False

q = int(input())

ans = []
for i in range(q):
    s = input()
    t = input()
    
    if has_common_char(s, t):
        ans.append('YES')
    else:
        ans.append('NO')

for i in range(q):
    print(ans[i])