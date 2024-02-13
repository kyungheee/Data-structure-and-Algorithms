def solution(genres, plays):
    answer = []
    count = {}
    rank = {}
    for i, (g, p) in enumerate(zip(genres, plays)):
        count[g] = count.get(g, 0) + p
        rank[g] = rank.get(g, []) + [(i, p)]
    genre = sorted(count.items(), key=lambda x: x[1], reverse=True) 
    for g, _ in genre:
        arr = rank[g]
        a = sorted(arr, key=lambda x: (-x[1], x[0]))
        answer.extend([idx for idx, _ in a[:2]])
    return answer
