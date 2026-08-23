def solution(numbers, target):
    cnt = 0
    def dfs(idx, total):
        nonlocal cnt
        if idx == len(numbers):
            if total == target: 
                cnt += 1
            return 
        dfs(idx+1, total + numbers[idx])
        dfs(idx+1, total - numbers[idx])
        
    dfs(0, 0)
    return cnt