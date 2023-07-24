def solution(a, b):
    answer = 0
    sort_a = sorted(a)
    sort_b = sorted(b, reverse=True)
    for _a, _b in zip(sort_a, sort_b):
        answer += _a * _b

    return answer
