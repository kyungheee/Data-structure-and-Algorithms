from collections import deque
def solution(cards1, cards2, goal):
    c1 = deque()
    c2 = deque()
    g2 = []
    for c in cards1:
        c1.append(c)
    for c in cards2:
        c2.append(c)
    for g in goal:
        if c1 and c1[0] == g :
            c = c1.popleft()
            g2.append(c)
        elif c2 and c2[0] == g:
            c = c2.popleft()
            g2.append(c)
    if g2 == goal:
        return 'Yes'  
    return 'No'
