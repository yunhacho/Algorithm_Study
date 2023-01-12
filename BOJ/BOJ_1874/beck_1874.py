n = int(input())

count = 1
stack = []
result = []
for _ in range(n):
    integer = int(input())
    while count <= integer:
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == integer:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)

print('\n'.join(result))
