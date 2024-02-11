def solution(participant, completion):
    answer= ''

    par1= {}

    for par in participant:
        if par in par1:
            par1[par]+= 1
        else:
            par1[par]= 1

    for fin in completion:
        par1[fin] -= 1
        if par1[fin] == 0:
            del par1[fin]

    par1=list(par1)[0]
    return answer.join(par1)