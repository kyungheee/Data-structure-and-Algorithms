from collections import deque

def solution(cards1, cards2, goal):
    
    # cards 와 goal을 deque로 변환
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)

    # goal 의 문자열을 순차적으로 순회
    while goal:
        if cards1 and cards2[0] == goal[0]: # card1의 front와 일치하는 경우
            cards1.popleft()
            goal.popleft()
        elif cards2 and cards2[0] == goal[0]: # card2의 front와 일치하는 경우
            cards2.popleft()
            goal.popleft()
        else:
            break # 일치하는 원소를 찾지 못했으므로 종료

    return "Yes" if not goal else "No" # goal이 비었으면 "Yes" 아니면 "No"를 반환