import collections

def solution(want, number, discount):
    answer= 0
    dict1= dict(zip(want, number))

    for i in range(len(discount)-9):
        if dict1 == collections.Counter(discount[i:i+10]):
            answer+= 1
    return answer