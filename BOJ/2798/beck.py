N, M = map(int, input().split())
cards = list(map(int, input().split()))

result = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            three_cards = cards[i] + cards[j] + cards[k]
            if three_cards <= M:
                result = max(result, three_cards)

print(result)
