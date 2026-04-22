def solution(n, words):
    used_word = set()
    used_word.add(words[0])
    
    for i in range(1, len(words)):
        if words[i] in used_word or words[i-1][-1] != words[i][0] or len(words) < 2:
            return [(i%n)+1, (i//n)+1]
        used_word.add(words[i])
    return [0, 0]