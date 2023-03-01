import re, sys

string = sys.stdin.readline()
text = sys.stdin.readline().strip()
cnt = 0

while True:
    if re.search(text, string):
        last = re.search(text, string).span()[1]
        string = string[last:]
        cnt += 1
    else:
        break

print(cnt)
