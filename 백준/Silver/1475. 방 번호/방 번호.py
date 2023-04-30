import sys
from collections import Counter

inputs = sys.stdin.readline

num = list(inputs().strip())

cnt = Counter(num)

result = 0
nine_six = 0
nine_six_cnt = 0

for item, val in cnt.items():
    if item in ['9', '6']:
        nine_six += val
    elif val > 0:
        result = max(val, result)
nine_six_cnt += nine_six // 2
nine_six_cnt += nine_six % 2

print(max(nine_six_cnt, result))
