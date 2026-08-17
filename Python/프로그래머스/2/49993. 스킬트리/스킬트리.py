def solution(skill, skill_trees):
    answer = 0
    for word in skill_trees:
        temp = ''
        for ch in word:
            if ch in skill:
                temp += ch
            
        if skill.startswith(temp):
            answer += 1
    return answer