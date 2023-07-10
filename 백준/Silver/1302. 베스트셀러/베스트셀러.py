# https://www.acmicpc.net/problem/1302
import sys
from collections import defaultdict

if __name__ == '__main__':
    q = defaultdict(int)

    get = sys.stdin.readline
    n = int(get())
    for i in range(n):
        book = get().strip()
        q[book] += 1
    answer = -sys.maxsize
    ans = []
    for i, v in q.items():
        if v == answer:
            answer = v
            ans.append(i)
        elif v > answer:
            answer = v
            ans = [i]
    sorted_ans = sorted(ans)
    print(sorted_ans[0])
