import sys

N = int(sys.stdin.readline())
numbers = [0] * 10000

for _ in range(N):
    numbers[int(sys.stdin.readline()) - 1] += 1

for i in range(1, 10001):
    if numbers[i-1] != 0:
        for j in range(numbers[i-1]):
            print(i)