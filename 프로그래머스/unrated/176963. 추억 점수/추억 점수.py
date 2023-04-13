from collections import defaultdict


def solution(name, yearning, photo):
    name_score = defaultdict()
    for n, y in zip(name, yearning):
        name_score[n] = y
    answer = []

    for item in photo:
        score = 0
        for person in item:
            if person in name_score:
                score += name_score[person]
            else:
                continue
        answer.append(score)
    return answer
