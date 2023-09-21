def check_reversed_string(s, rs):
    len_s = len(s)
    len_rs = len(rs)

    if len_s != len_rs:
        return 'NO'

    for i in range(len_s):
        j = len_s - 1 - i
        if s[i] != rs[j]:
            return 'NO'
    
    return 'YES'

s = input()
rs = input()
print(check_reversed_string(s, rs))