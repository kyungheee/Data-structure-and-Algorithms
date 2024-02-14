# 내가 짠 코드
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer= []

    for num in course:
        menu = []

        for order in orders:
            menu += combinations(sorted(order),num)
        counter= Counter(menu)

        for key, value in counter.items():
            if (value >= 2) and (value == max(counter.values())):
                answer.append("".join(key))

    return sorted(answer)