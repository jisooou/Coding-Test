def solution(genres, plays):
    total = {}
    song = {}
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        total[genre] = total.get(genre, 0) + play
        if genre not in song:
            song[genre] = []
        song[genre].append((play, idx))
        
    genre_sort = sorted(total.keys(), key=lambda x: total[x], reverse=True)    

    answer = []
    for genre in genre_sort:
        song[genre].sort(key=lambda x: (-x[0], x[1]))
        for play, idx in song[genre][:2]:
            answer.append(idx)
    return answer