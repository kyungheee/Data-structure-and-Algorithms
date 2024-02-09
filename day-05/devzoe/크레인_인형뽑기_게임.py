def solution(board, moves):
    answer = 0
    stack = []
    for m in moves :
        for b in board:
            if b[m-1] != 0:
                if stack and stack[-1] == b[m-1]:
                    stack.pop()
                    answer += 2
                    b[m-1] = 0
                else :
                    stack.append(b[m-1])
                    b[m-1] = 0
                break       
    return answer
