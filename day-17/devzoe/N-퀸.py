result = 0
def adjacent(x,row):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == x-i:
            return False
    return True

def dfs(x,N,row):
    global result
    if x == N:
        result += 1
    else:
        for i in range(N):
            row[x] = i
            if adjacent(x,row):
                dfs(x+1,N,row)
def solution(n):  
    row = [0] * n
    dfs(0,n,row)
    return result
