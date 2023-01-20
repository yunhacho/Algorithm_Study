def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return p


def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        relation[x] += relation[y]


TC = int(input())

for _ in range(TC):
    parent = dict()
    relation = dict()

    F = int(input())

    for _ in range(F):
        x, y = input().split()

        if x not in parent:
            parent[x] = x
            relation[x] = 1
        if y not in parent:
            parent[y] = y
            relation[y] = 1

        union(x, y)

        print(relation[find(x)])
