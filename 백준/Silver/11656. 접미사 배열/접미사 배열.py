import sys
from heapq import heappush, heapify

inputs = sys.stdin.readline
string = inputs().strip()

lst = []
for idx in range(len(string)):
    heappush(lst, string[idx:])

lst.sort()

for item in lst:
    if len(item) > 0:
        print(item)
