N = int(input())
A = set(map(int, input().split()))
M = int(input())

for i in list(map(int, input().split())):
    if i in A:
        print('1')
    else:
        print('0')
