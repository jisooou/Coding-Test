def solution(word):
    vowel = 'AEIOU'
    cnt = 0          
    def dfs(current):
        nonlocal cnt
        if len(current) > 5:
            return 
        if current:
            cnt += 1
            if current == word:
                return cnt 
        for v in vowel:
            result = dfs(current + v)
            if result:
                return result
        
    return dfs("")