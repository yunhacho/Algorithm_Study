TC = int(input())

for _ in range(TC):
    N, M = map(int, input().split())
    documents = list(map(int, input().split()))
    documents = [(idx, doc) for idx, doc in enumerate(documents)]

    count = 0
    while True:
        if documents[0][1] == max(documents, key=lambda x: x[1])[1]:
            count += 1
            if documents[0][0] == M:
                print(count)
                break
            else:
                documents.pop(0)
        else:
            documents.append(documents.pop(0))
