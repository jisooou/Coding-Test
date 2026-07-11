def solution(players, callings):
    players_dict = {}
    for idx, player in enumerate(players):
        players_dict[player] = idx
    
    for call_name in callings:
        call_idx = players_dict[call_name] 
        front = players[call_idx-1] 
        
        players[call_idx], players[call_idx-1] = players[call_idx-1], players[call_idx]
        players_dict[call_name] = call_idx-1
        players_dict[front] = call_idx
    
    return players