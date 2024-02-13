def solution(participant, completion):
    answer = ''
    dict = {}
    for c in completion:
        dict[c] = dict.get(c, 0) + 1
    for p in participant:
        if p not in dict.keys() or dict[p] == 0:
            answer = p
            break
        dict[p] -= 1   
    return answer
