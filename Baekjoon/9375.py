import sys
for t in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    wear_dt = dict()
    count_dt = dict()
    
    for i in range(n):
        wear, wear_type = sys.stdin.readline().rstrip().split()
        wear_dt[wear] = wear_type
    
    for wear in wear_dt.values():
        if wear not in count_dt:
            count_dt[wear] = 1
        else:
            count_dt[wear] += 1
    
    total = 1
    for cnt in count_dt.values():
        total *= cnt+1
    
    print(total - 1)