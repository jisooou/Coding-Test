def solution(word):
    vowel = 'AEIOU'
    words = []
    def dfs(current):
        if len(current) > 5:
            return
        if current: 
            words.append(current)
            
        for v in vowel:
            dfs(current+v)
    dfs('')
    return words.index(word)+1