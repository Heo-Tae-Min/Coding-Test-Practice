import sys

N, M = map(int, sys.stdin.readline().split())
member_dt = dict()
group_dt = dict()

for i in range(N):
    group_name = sys.stdin.readline().rstrip()
    member_num = int(sys.stdin.readline())
    
    members = []
    for num in range(member_num):
        member = sys.stdin.readline().rstrip()
        members.append(member)
        member_dt[member] = group_name
    group_dt[group_name] = members
    
for i in range(M):
    quiz = sys.stdin.readline().rstrip()
    quiz_type = int(sys.stdin.readline())
    
    if(quiz_type == 0):
        for member in sorted(group_dt[quiz]):
            print(member)
    elif(quiz_type == 1):
        print(member_dt[quiz])