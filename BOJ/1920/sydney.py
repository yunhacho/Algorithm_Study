import sys

N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
m_numbers = list(map(int, sys.stdin.readline().split()))

for m in m_numbers:
    answer = 0
    start = 0
    end = len(A) - 1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == m:
            answer = 1
            break
        elif A[mid] > m:
            end = mid - 1
        else:
            start = mid + 1
    print(answer)
