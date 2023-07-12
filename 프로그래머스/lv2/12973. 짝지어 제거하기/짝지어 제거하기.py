from collections import deque


def solution(s):
    answer = -1
    q = deque()
    for i in s:
        if not q:
            q.append(i)
        else:
            if q[-1] == i:
                q.pop()
            else:
                q.append(i)

    return 1 if not q else 0