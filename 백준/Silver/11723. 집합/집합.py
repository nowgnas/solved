import sys

if __name__ == '__main__':
    inputs = sys.stdin.readline
    n = int(inputs())
    s = 0
    for i in range(n):
        command = inputs().split()
        if command[0] == 'add':
            s |= (1 << int(command[1]))
        elif command[0] == 'remove':
            s &= ~(1 << int(command[1]))
        elif command[0] == 'check':
            print(1 if s & (1 << int(command[1])) != 0 else 0)
        elif command[0] == 'toggle':
            s ^= (1 << int(command[1]))
        elif command[0] == 'all':
            s = (1 << 21) - 1  # 채우기
        elif command[0] == 'empty':
            s = 0

# https://www.acmicpc.net/problem/11723
# 비트 마스킹
