import sys

n = int(sys.stdin.readline())

F = [0, 1]

for i in range(n-1):
    F.append(sum(F[-2::]))

print(F[-1])
