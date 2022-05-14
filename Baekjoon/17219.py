import sys
N, M = map(int, sys.stdin.readline().split())
dt = dict()
for i in range(N):
    addr, pw = sys.stdin.readline().rstrip().split()
    dt[addr] = pw

for i in range(M):
    print(dt[sys.stdin.readline().rstrip()])