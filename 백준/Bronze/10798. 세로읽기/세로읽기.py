import sys

if __name__ == '__main__':
    get = sys.stdin.readline
    maps = [['' for _ in range(15)] for i in range(5)]
    for i in range(5):
        line = list(get().strip())
        for j in range(len(line)):
            maps[i][j] = line[j]
    answer = ''
    for i in range(15):
        for j in range(5):
            if maps[j][i] != '':
                answer += maps[j][i]
    print(answer)