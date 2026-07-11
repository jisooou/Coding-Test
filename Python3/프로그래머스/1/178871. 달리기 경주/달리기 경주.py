def solution(players, callings):
    players_dict = {}
    for idx, name in enumerate(players):
        players_dict[name] = idx
    
    for i in callings: 
        idx = players_dict[i]
        front_player = players[idx-1]
        
        players[idx], players[idx-1] = players[idx-1], players[idx]
        
        players_dict[i] = idx-1
        players_dict[front_player] = idx
    return players