def solution(genres, plays):
    genre = {}
    play = {}
    for i in range(len(genres)):
        if genres[i] in genre.keys():
            genre[genres[i]].append((plays[i], i))
            play[genres[i]] += plays[i]
        else:
            genre[genres[i]] = [(plays[i], i)]
            play[genres[i]] = plays[i]
    sort_play = sorted(play.items(), key = lambda x : -x[1])
    answer = []
    for k, v in sort_play:
        tmp = sorted(genre[k], key = lambda x : (-x[0], x[1]))
        answer.append(tmp[0][1])
        if len(tmp) > 1:
            answer.append(tmp[1][1])
    return answer