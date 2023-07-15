import sys
import re

u = re.compile('[A-Z]')
l = re.compile('[a-z]')
d = re.compile('[0-9]')

while True:
    num_u = 0
    num_l = 0
    num_n = 0
    num_b = 0
    try:
        n = input()
        for i in n:
            if ' ' == i:
                num_b += 1
            elif l.match(i):
                num_l += 1
            elif u.match(i):
                num_u += 1
            elif d.match(i):
                num_n += 1
        print(f'{num_l} {num_u} {num_n} {num_b}')
    except:
        break
