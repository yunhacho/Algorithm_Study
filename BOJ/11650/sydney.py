import sys

N = int(sys.stdin.readline())
coord_list = []

for i in range(N):
    coord = list(map(int, sys.stdin.readline().split()))
    coord_list.append(coord)

coord_list.sort(key=lambda x: (x[0], x[1]))

for x in coord_list:
    print(x[0], x[1])