import sys
rd = sys.stdin.readline
part = []

S = rd().rstrip()
for i in range(1, len(S)+1):
    for j in range(len(S) - i + 1):
        part.append(S[j:j+i])
part = set(part)
print(part)
print(len(part))