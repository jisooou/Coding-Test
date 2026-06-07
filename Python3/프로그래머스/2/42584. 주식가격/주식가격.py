def solution(prices):
    n = len(prices)
    stack = []
    answer = [0]*n
    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]:
            prev = stack.pop()
            answer[prev] = i - prev
        stack.append(i)
            
    while stack:
        prev = stack.pop()
        answer[prev] = n - 1 - prev
    return answer