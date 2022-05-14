import sys

n = int(sys.stdin.readline())
people = {}

for i in range(n):
    name, action = sys.stdin.readline().rstrip().split()
    if action == "enter":
        people[name] = action
    elif action == "leave":
        if people[name]:
            del people[name]

people = list(people.keys())
people.sort(reverse=True)

for person in people:
    print(person)