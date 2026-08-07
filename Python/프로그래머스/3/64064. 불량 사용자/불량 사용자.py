def solution(user_id, banned_id):
    def is_match(user, ban):
        if len(user) != len(ban):
            return False
        for x, y in zip(user, ban):
            if y == '*':
                continue
            if x != y:
                return False
        return True
    
    total = []
    for ban in banned_id:
        temp = []
        for user in user_id:
            if is_match(user, ban):
                temp.append(user)
        total.append(temp)
    
    answer = set()
    def dfs(idx, select):
        if idx == len(total):
            answer.add(tuple(sorted(select)))
            return 
        for user in total[idx]:
            if user not in select:
                select.add(user)
                dfs(idx+1, select)
                select.remove(user)
    
    dfs(0, set())
    return len(answer)