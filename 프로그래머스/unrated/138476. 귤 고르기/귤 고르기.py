from collections import defaultdict


def solution(k, tangerine):
    answer = 0
    t_dict = defaultdict(int)
    for t in tangerine:
        t_dict[t] += 1

    kind = 0
    dict_sort = sorted(t_dict.items(), key=lambda x: x[1], reverse=True)
    for t, val in dict_sort:
        if answer < k:
            answer += val
            kind += 1
        
    return kind
