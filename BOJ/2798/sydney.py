import sys

def solution():
    
    n, m = map(int, sys.stdin.readline().split())
    numbers = list(map(int, sys.stdin.readline().split()))

    numbers.sort(reverse=True)
    answer = 0

    for i in range(n):
        if numbers[i] < m:
            for j in range(i+1, n):
                if numbers[i] + numbers[j] + numbers[-1] <= m:
                    for k in range(j+1, n):
                        cards_sum = numbers[i] + numbers[j] + numbers[k]
                        if cards_sum == m:
                            print(m)
                            return
                        elif (cards_sum < m) and (cards_sum > answer):
                            answer = cards_sum
                        else:
                            pass
                else:
                    pass
        else:
            pass
    print(answer)

if __name__ == '__main__':
    solution()
    