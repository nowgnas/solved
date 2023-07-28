import sys


def reverse(x):
    num = int(x[::-1])
    return num


a, b = map(str, sys.stdin.readline().split())

a = reverse(a)
b = reverse(b)
answer = reverse(str(a + b))
print(answer)
