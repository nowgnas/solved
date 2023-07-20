def solution(n):
    b_num = format(n, 'b')
    for num in range(n + 1, 1000001):
        is_next = format(num, 'b')
        if b_num.count('1') == is_next.count('1'):
            return num
