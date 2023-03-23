import sys

string1 = sys.stdin.readline().strip()
string2 = sys.stdin.readline().strip()

dp = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]

for i, s1 in enumerate(string1):
    for j, s2 in enumerate(string2):
        if s1 == s2:
            dp[i + 1][j + 1] = dp[i][j]+ 1
        else:
             dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

print(dp[-1][-1])