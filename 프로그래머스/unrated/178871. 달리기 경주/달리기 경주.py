def solution(players, callings):
    rank = { p : i for i, p in enumerate(players) }
    for c in callings:
        pre , idx = rank[c] - 1 , rank[c]
        players[pre], players[idx] = players[idx] , players[pre]
        rank[players[pre]] , rank[players[idx]] = rank[players[pre]] - 1 , rank[players[idx]] + 1
    return players