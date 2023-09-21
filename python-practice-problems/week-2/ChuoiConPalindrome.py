def count_palindrome_substrings(s):
    n = len(s)
    count = 0
    dp = [[False for _ in range(n)] for _ in range(n)]
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if length == 1:
                dp[i][j] = True
            elif length == 2:
                dp[i][j] = (s[i] == s[j])
            else:
                dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
            
            if dp[i][j]:
                count += 1
    return count

s = input()
print(count_palindrome_substrings(s))