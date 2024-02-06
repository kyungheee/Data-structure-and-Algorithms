def solution(answers):
    
    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]

    # [0,0,0] 이랑 같은 표현
    scores = [0]*3

    #패턴이랑 정답이 얼마나 일치하는지
    for i , answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i%len(pattern)]:
                scores += 1
                
    # 가장 높은 점수 저장            
    max_score = max(scores)

    # 가장 높은 점수를 가진 사람이 한 명이 아닐 수도 있다!
    highest_scores = []
    for i, score in enumerate(scores):
        if score == max_score:
            highest_scores.append(i+1)

    return highest_scores