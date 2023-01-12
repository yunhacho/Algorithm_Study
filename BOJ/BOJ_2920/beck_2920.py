scales = list(map(int, input().split()))

asc, desc = True, True

for i in range(len(scales) - 1):
    if scales[i] < scales[i + 1]:
        desc = False
    else:
        asc = False

if asc:
    print('ascending')
elif desc:
    print('descending')
else:
    print('mixed')
