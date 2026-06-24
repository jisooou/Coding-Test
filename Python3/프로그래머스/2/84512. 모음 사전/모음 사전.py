def solution(word):
    vowel = 'AEIOU'
    words = []
    answer = 0
    def dfs(current):
        nonlocal answer
        if len(current) > 5:
            return 
        
        if current: 
            words.append(current)
            
        for v in vowel:
            dfs(current+v)
    dfs('')
    return words.index(word)+1