def solution(numbers, target):
    cnt = 0
    def dfs(index, total):
        nonlocal cnt
        if index == len(numbers):
            if total == target:
                cnt += 1
            return
            
        dfs(index+1, total+numbers[index])
        dfs(index+1, total-numbers[index])
            
    dfs(0, 0)
    return cnt