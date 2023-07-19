def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    stack = []
    
    for idx in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[idx]:
                num = stack.pop()
                answer[num] = numbers[idx]
                
        
        stack.append(idx)
    
    return answer