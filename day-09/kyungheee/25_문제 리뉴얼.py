from itertools import combinations
from collections import Counter

def solution(order, course):
    answer = [ ]

    for c in course:
        menu = [ ]
        for order in order:
            comb = combinations(
                sorted(order), c
            )
            menu += comb
        
        counter = Counter(menu)
        if (
            len(counter) != 0 and max(counter.values()) != 1
        ): # 가장 많이 주문된 구성이 1번 이상 주문된 경우
            for m, cnt in counter.items():
                if cnt == max(counter.values()):
                    answer.append("".join(m))

    return sorted(answer)