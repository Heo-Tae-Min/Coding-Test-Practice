import sys
K, L = map(int, sys.stdin.readline().split())

wait_list = {}
for i in range(L):
    student = sys.stdin.readline().rstrip()
    wait_list[student] = i

wait_list = sorted(wait_list.items(), key=lambda x : x[1])

cnt = 0
for i in wait_list:
    if cnt == K:
        break
    print(i[0])
    cnt += 1