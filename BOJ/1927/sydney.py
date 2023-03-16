import sys, heapq

n = int(sys.stdin.readline())
num_list = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(num_list) == 0:
            print(0)
        else:
            print(heapq.heappop(num_list))
    else:
        heapq.heappush(num_list, num)