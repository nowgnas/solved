if __name__ == '__main__':
    val = input()
    answer = 0
    for i in val:
        answer += int(i)
    if answer % 3 == 0 and val.count('0') > 0:
        answer = sorted(val, reverse=True)
        print(''.join(answer))
    else:
        print(-1)
