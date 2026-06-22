def solution(word):
    vowel = 'AEIOU'
    lst = []
    def dfs(current):
        if len(current) > 5:
            return 
        if current:
            lst.append(current)
        for v in vowel:
            dfs(current+v)
    dfs("")
    return lst.index(word)+1