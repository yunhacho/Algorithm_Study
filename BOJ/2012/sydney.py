import sys

N = int(sys.stdin.readline())

guess = []
for _ in range(N):
    guess.append(int(sys.stdin.readline()))

guess.sort()

print(sum(map(lambda x, y: abs(x - y), guess, [i for i in range(1, N + 1)])))