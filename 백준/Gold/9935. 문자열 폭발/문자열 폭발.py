import sys

inputs = sys.stdin.readline
string = inputs().rstrip()
bomb = list(inputs().rstrip())

stack = []
result = []
idx = 0
equal_flag = False
for item in string:
    stack.append(item)
    if stack[-len(bomb):] == bomb:
        for word in range(len(bomb)):
            stack.pop()
print("".join(stack) if len(stack) > 0 else "FRULA")
