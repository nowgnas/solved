def solution(s):
    answer = []
    zero = 0
    length = 0
    idx = 0
    while True:
        if s == '1':
            break
        idx += 1
        zero += s.count('0')
        s = s.replace('0', '')
        length = len(s)
        s = format(length, 'b')
    return [idx, zero]
