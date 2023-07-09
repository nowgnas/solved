import sys

if __name__ == '__main__':
    get = sys.stdin.readline
    n = get().strip()
    m = get().strip()
    pattern = ''
    idx = 0
    answer = 0
    length = len(m)
    while idx < len(n):
        pattern += n[idx]
        if len(pattern) >= len(m):
            if pattern[-length:] == m:
                pattern = ''
                answer += 1
        idx += 1
    print(answer)
