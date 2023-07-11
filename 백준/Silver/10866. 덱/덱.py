import sys
from collections import deque

if __name__ == '__main__':
    get = sys.stdin.readline
    n = int(get())

    q = deque()
    for i in range(n):
        command = list(map(str, get().split()))
        if command[0] == 'push_front':
            q.appendleft(command[1])
        elif command[0] == 'push_back':
            q.append(command[1])
        elif command[0] == 'pop_front':
            if q:
                val = q.popleft()
                print(val)
            else:
                print(-1)
        elif command[0] == 'pop_back':
            if q:
                val = q.pop()
                print(val)
            else:
                print(-1)
        elif command[0] == 'size':
            print(len(q))
        elif command[0] == 'empty':
            print(1 if not q else 0)
        elif command[0] == 'front':
            if q:
                print(q[0])
            else:
                print(-1)
        elif command[0] == 'back':
            if q:
                print(q[-1])
            else:
                print(-1)
