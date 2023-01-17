import sys

def binary_search(sequence, n):
    left = 0
    right = len(sequence)-1

    while left <= right:
        mid = (right + left) // 2
        if sequence[mid] == n:
            return 1
        elif sequence[mid] > n:
            right = mid - 1
        elif sequence[mid] < n:
            left = mid + 1
    return 0

if __name__ == "__main__":
    n = int(input())
    sequence = list(map(int, sys.stdin.readline().split()))
    m = int(input())
    numbers  = list(map(int, sys.stdin.readline().split()))

    sequence = sorted(sequence)
    for num in numbers:
        res = binary_search(sequence, num)
        print(res)