# https://www.acmicpc.net/problem/14502
import sys
from itertools import combinations
import copy
from collections import deque

inputs = sys.stdin.readline

n, m = map(int, inputs().split(" "))
blank = set()
matrix = [[0 for x in range(m)] for y in range(n)]

for i in range(n):
    line = list(map(int, inputs().split(" ")))
    for j in range(m):
        matrix[i][j] = line[j]
        if matrix[i][j] == 0:
            blank.add((i, j))
# 입력 완료


comb = list(combinations(blank, 3))

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]


def check_range(y, x):
    return y < n and x < m and 0 <= y and 0 <= x


def bfs(matrix, y, x, visited):
    cnt = 0
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    while q:
        _y, _x = q.popleft()
        for idx in range(4):
            ny = _y + dy[idx]
            nx = _x + dx[idx]
            if not check_range(ny, nx):
                continue
            if not visited[ny][nx] and matrix[ny][nx] == 0:
                q.append((ny, nx))
                matrix[ny][nx] = 2
                cnt += 1
                visited[ny][nx] = True
    return cnt


def each_case(matrix, a, b, c, visited, zero_cnt):
    # 벽 3개 세우기
    matrix[a[0]][a[1]] = 1
    matrix[b[0]][b[1]] = 1
    matrix[c[0]][c[1]] = 1
    for y in range(n):
        for x in range(m):
            if matrix[y][x] == 2 and visited[y][x] is False:
                zero_cnt -= bfs(matrix, y, x, visited)
    return zero_cnt

answer= -sys.maxsize
for a, b, c in comb:
    zero_cnt = len(blank)  # 0의 개수
    co_matrix = copy.deepcopy(matrix)
    visited = [[False for y in range(m)] for x in range(n)]
    result = each_case(co_matrix, a, b, c, visited, zero_cnt) - 3
    answer = max(answer, result)
print(answer)
