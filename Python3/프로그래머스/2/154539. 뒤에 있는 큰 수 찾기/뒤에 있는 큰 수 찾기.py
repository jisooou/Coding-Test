def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i in range(len(numbers)):
        current = numbers[i]
        while stack and numbers[stack[-1]] < current:
            idx = stack.pop()
            answer[idx] = current
        stack.append(i)
    return answer 