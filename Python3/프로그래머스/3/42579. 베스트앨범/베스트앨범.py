def solution(genres, plays):
    total = {}
    song = {}
    
    for idx, genre in enumerate(genres):
        play = plays[idx]
        if genre not in total:
            total[genre] = 0
            song[genre] = []
        total[genre] += play
        song[genre].append((play, idx))
    sorted_genre = sorted(total.keys(), key=lambda x: total[x], reverse=True)
    
    answer = []
    for genre in sorted_genre:
        sorted_song = sorted(song[genre], key=lambda x: (-x[0], x[1]))

        for play, idx in sorted_song[:2]:
            answer.append(idx)
    return answer