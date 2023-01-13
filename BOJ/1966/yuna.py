import sys
from collections import deque
input = sys.stdin.readline

def boj_1966(n, m, prior):
    idx = -1
    order = 0
    printer = deque([(i, p) for i, p in zip(range(n), prior)])
    que = deque(sorted(prior, reverse=True))

    while idx != m:
        if que[0] == printer[0][1]:
            que.popleft()
            idx, p = printer.popleft()
            order+=1
        else:
            printer.append(printer.popleft())
    return order

if __name__ == "__main__":
    T = int(input())
    output = []
    for _ in range(T):
        n, m = map(int, input().split())
        prior = list(map(int, input().split()))
        output.append( boj_1966(n,m,prior))

    print(*output, sep='\n', end='')
