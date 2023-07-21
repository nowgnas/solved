import sys

if __name__ == '__main__':
    get = sys.stdin.readline
    answer = False
    s = get().strip()
    if len(s) % 2 == 0:
        # 길이가 짝수일 경우
        pivot = len(s) // 2
        compare = s[:pivot]
        compare2 = s[pivot:][::-1]
        if compare == compare2:
            answer = True
    else:
        # 길이가 홀수인 경우
        pivot = len(s) // 2
        compare = s[:pivot]
        compare2 = s[pivot + 1:][::-1]
        if compare == compare2:
            answer = True
    print(1 if answer else 0)
