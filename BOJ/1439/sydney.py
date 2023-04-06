import sys

S = sys.stdin.readline()

start = S[0]
cnt = 0

for s in S[1:]:
    if start != s:
        cnt += 1
    start = s

print(cnt // 2)
