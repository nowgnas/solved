import sys
from collections import deque

inputs = sys.stdin.readline

n = int(inputs().strip())

graph = [[] for i in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, inputs().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)

answer = [0 for i in range(n + 1)]

while q:
    cur: int = q.popleft()
    for x in graph[cur]:
        if answer[x] == 0:
            answer[x] = cur
            q.append(x)

for i in range(2, n + 1):
    print(answer[i])
