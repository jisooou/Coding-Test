def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            prev = stack.pop()
            answer[prev] = i-prev
        stack.append(i)
    while stack:
        prev = stack.pop()
        answer[prev] = len(prices) - 1 - prev
    return answer