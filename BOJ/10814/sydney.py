import sys

N = int(sys.stdin.readline())
cust = []

for i in range(N):
    info = sys.stdin.readline().split()
    info.append(i)
    cust.append(info)

cust.sort(key=lambda x: (int(x[0]), x[2]))

for x in cust:
    print(x[0], x[1])