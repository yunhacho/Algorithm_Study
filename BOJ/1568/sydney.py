import sys

N = int(sys.stdin.readline())

K = 1
cnt = 0

while True:
    if N - K < 0:
        K = 1
    elif N - K == 0:
        cnt += 1
        break
    else:
        N = N - K
        K += 1
        cnt += 1

print(cnt)