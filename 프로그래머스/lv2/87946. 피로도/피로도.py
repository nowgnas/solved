from itertools import permutations

def solution(k, dungeons):
    answer = -1
    perm = permutations(dungeons, len(dungeons))
    for item in perm:
        start_hp = k
        cnt = 0
        for hp, sub in item:
            if start_hp >= hp:
                start_hp -= sub
                cnt += 1
        answer = max(cnt, answer)
    return answer