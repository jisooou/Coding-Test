def solution(user_id, banned_id):
    def is_match(user, ban):
        for x, y in zip(user, ban):
            if y == '*':
                continue
            if x != y:
                return False
        return True
    
    candidate = []
    for ban in banned_id:
        temp = []
        for user in user_id:
            if len(user) != len(ban):
                continue
            if is_match(user, ban):
                temp.append(user)
        candidate.append(temp)
    
    answer = set()
    def dfs(idx, select):
        if idx == len(candidate):
            answer.add(tuple(sorted(select)))
            return 
        
        for user in candidate[idx]:
            if user not in select:
                select.add(user)
                dfs(idx+1, select)
                select.remove(user)
            
    
    dfs(0, set())
    return len(answer)