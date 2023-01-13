import sys

def boj_2920(input):
    diff = input[0]-input[1]
    for i in range(2, len(input)-1):
        if input[i]-input[i+1] != diff:
            return "mixed"

    return "ascending" if diff == -1 else "descending"

if __name__ == "__main__":
    input = list(map(int, sys.stdin.readline().split()))
    output = boj_2920(input)
    print(output)
