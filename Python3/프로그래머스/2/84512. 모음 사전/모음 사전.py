def solution(word):
    vowel = 'AEIOU'
    answer = []
    def dfs(current):
        if len(current) > 5:
            return 
        if current:
            answer.append(current)
        for v in vowel:
            dfs(current + v)
        
    dfs("")
    return answer.index(word)+1