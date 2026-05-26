def solution(ingredient):
    order = [1, 2, 3, 1]
    stack = []
    cnt = 0
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == order:
            cnt += 1
            # for _ in range(4):
            #     stack.pop()
            del stack[-4:]
    return cnt