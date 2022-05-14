import sys

n, q = sys.stdin.readline().split()
n = int(n)
q = int(q)

pocketmon = {}
pocketmon_name = ["Zero"]
for i in range(1, n+1):
    name = sys.stdin.readline().rstrip()
    pocketmon[name] = i
    pocketmon_name.append(name)

for i in range(q):
    question = sys.stdin.readline().rstrip()
    if question.isdigit():
        print(pocketmon_name[int(question)])
    else:
        print(pocketmon[question])