TC = int(input())

for _ in range(TC):
    left = []
    right = []
    for key in input():
        if key == '<':
            if left:
                right.append(left.pop())
        elif key == '>':
            if right:
                left.append(right.pop())
        elif key == '-':
            if left:
                left.pop()
        else:
            left.append(key)
    left.extend(reversed(right))
    print(''.join(left))
