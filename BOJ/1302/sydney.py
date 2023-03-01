import sys
from collections import Counter

N = int(sys.stdin.readline())
books = []
for _ in range(N):
    books.append(sys.stdin.readline())

c = Counter(books)
m = max(c.values())
print(sorted([k for k, v in c.items() if v == m])[0])