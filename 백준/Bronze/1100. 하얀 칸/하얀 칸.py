import sys

if __name__ == '__main__':
    get = sys.stdin.readline
    maps = [['' for _ in range(8)] for _ in range(8)]

    for i in range(8):
        line = get().strip()
        for j in range(8):
            maps[i][j] = line[j]
    answer = 0
    for i in range(8):
        for j in range(8):
            if maps[i][j] == 'F':
                if i % 2 == 1 and j % 2 == 1:
                    answer += 1
                elif i % 2 == 0 and j % 2 == 0:
                    answer += 1
    print(answer)
