import sys

if __name__ == '__main__':
    get = sys.stdin.readline
    n = int(get())

    lst = []
    for i in range(n):
        line = get().strip()
        lst.append(line)
    start = lst[0]
    answer = list(lst[0])

    for i in range(1, len(lst)):
        for v, val in enumerate(lst[i]):
            if start[v] != val:
                answer[v] = '?'
    print(''.join(answer))
