import sys
from collections import defaultdict


def solution(s):
    size = len(s)
    for num in range(1, len(s)):
        word_set = []
        answer = ''
        group = defaultdict(int)
        for idx in range(0, len(s), num):
            word_set.append(s[idx: idx + num])
        # print(word_set)
        prev = ''

        # 2개 글자 세트 부터
        for word in word_set:
            if not group:
                prev = word
                group[word] += 1
            elif prev == word:
                group[prev] += 1
            elif prev != word:
                answer += str(group[prev]) if group[prev] > 1 else ''
                answer += prev
                group[prev] *= 0
                group[word] += 1
                prev = word
        for item, val in group.items():
            if val > 1:
                answer += str(val)
                answer += item
            elif val > 0:
                answer += item

        size = min(size, len(answer))

    return size
