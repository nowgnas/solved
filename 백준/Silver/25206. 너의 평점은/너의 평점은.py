import sys

score = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0
}

get = sys.stdin.readline
answer = 0
num = 0
for i in range(20):
    _, g, s = map(str, get().split())
    if s == 'P':
        continue
    num += float(g)
    get_score = float(g) * score[s]
    answer += get_score
print(round(answer / num, 6))
