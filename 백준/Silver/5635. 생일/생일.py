import sys
from collections import deque


class Person:
    def __init__(self, name, d, m, y):
        self.name = name
        self.day = int(d)
        self.month = int(m)
        self.year = int(y)


get = sys.stdin.readline

n = int(get())

q = deque()
for i in range(n):
    n, d, m, y = get().split()
    q.append(Person(n, d, m, y))

sort_person = sorted(q, key=lambda x: (x.year, x.month, x.day))
print(sort_person[-1].name)
print(sort_person[0].name)
