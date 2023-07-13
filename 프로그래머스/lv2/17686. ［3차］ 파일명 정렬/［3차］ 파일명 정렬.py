import re
from collections import deque


class file_name:
    def __init__(self, name, v):
        self.init = ''
        self.head = ''
        self.number = ''
        self.tail = ''
        self.num = 0
        self.idx = v
        flag = True
        com = re.compile('^[0-9]')
        for i in name:
            if not com.match(i) and not flag:
                break
            elif not com.match(i) and flag:
                self.head += i
            else:
                self.number += i
                flag = False
        self.init = name
        self.head = self.head.lower()
        self.num = int(self.number)


def solution(files):
    answer = []
    q = deque()

    for v, i in enumerate(files):
        name = file_name(i, v)
        q.append(name)
    for i in q:
        print(i.head, '-', i.num)
    sorted_q = sorted(q, key=lambda x: (x.head, x.num, x.idx))
    for i in sorted_q:
        answer.append(i.init)

    return answer
