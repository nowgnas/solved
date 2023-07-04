import sys
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


class Node:
    def __init__(self, y, x):
        self.y = y
        self.x = x


def check_range(ny, nx, n, m):
    return ny >= 0 and nx >= 0 and ny < n and nx < m


def one_year(maps, n, m):
    melt = [[-1 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            melt_cnt = 0
            if maps[i][j] > 0:
                for idx in range(4):
                    ny = i + dy[idx]
                    nx = j + dx[idx]
                    if check_range(ny, nx, n, m) and maps[ny][nx] == 0:
                        melt_cnt += 1
                melt[i][j] = melt_cnt
    for i in range(n):
        for j in range(m):
            if melt[i][j] > 0:
                maps[i][j] = maps[i][j] - melt[i][j] if maps[i][j] >= melt[i][j] else 0
    return maps


def find_island(maps, visited, n, m, r, c):
    q = deque()
    q.append(Node(r, c))
    visited[r][c] = True

    while q:
        cur = q.popleft()
        for i in range(4):
            ny = cur.y + dy[i]
            nx = cur.x + dx[i]
            if check_range(ny, nx, n, m) and visited[ny][nx] == False and maps[ny][nx] > 0:
                q.append(Node(ny, nx))
                visited[ny][nx] = True
    return visited


def bfs(maps, n, m):
    island = 0
    cnt = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                cnt += 1
            if maps[i][j] > 0 and visited[i][j] == False:
                visited = find_island(maps, visited, n, m, i, j)
                island += 1
    if n * m == cnt:
        return 0, False
    return island, True


if __name__ == '__main__':
    get = sys.stdin.readline
    n, m = map(int, get().split())
    maps = [[0 for _ in range(m)] for _ in range(n)]

    q = deque()
    for r in range(n):
        line = list(map(int, get().split()))
        for c in range(m):
            maps[r][c] = line[c]
    # 빙산 지도 저장
    # 1년치 빙산 녹이기
    year = 0
    island = 0

    while island < 2:
        maps = one_year(maps, n, m)
        island, flag = bfs(maps, n, m)
        if flag:
            year += 1
        else:
            year = 0
            break
    print(year)
    # 섬 개수 구하기

# https://www.acmicpc.net/problem/2573
