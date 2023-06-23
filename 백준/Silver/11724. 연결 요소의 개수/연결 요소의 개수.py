import sys
from collections import deque

inputs = sys.stdin.readline
n, m, = map(int, inputs().split())
if m == 0:
    print(n)
    exit(0)
visited = [False for i in range(n + 1)]

graph = [[] for i in range(n + 1)]
lst = []
for i in range(m):
    u, v, = map(int, inputs().split())
    lst.append(u)
    graph[u].append(v)
    graph[v].append(u)


def bfs(idx):
    q = deque()
    q.append(idx)
    visited[idx] = True
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


answer = 0
for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        answer += 1
print(answer)
