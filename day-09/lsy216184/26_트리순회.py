def preorder(nodes, idx):
    if idx < len(nodes):                 # (idx)현재 방문하고 있는 노드 < 노드 개수
        ret = str(nodes[idx]) + " "      # 루트노드 출력
        ret += preorder(nodes, idx*2+1)  # nodes 리스트를 다시 재귀함수에 전달(왼쪽 자식 노드)
        ret += preorder(nodes, idx*2+2)  # nodes 리스트를 다시 재귀함수에 전달(오른쪽 자식 노드)
        return ret
    else:
        return ""                        # dix >= len(nodes) 크다면 마지막은 공백 문자열 반환
# print(preorder([1, 2, 3, 4, 5, 6, 7], 0))
#1 2 4 5 3 6 7 

def inorder(nodes, idx):
    if idx < len(nodes):
        ret  = inorder(nodes, idx*2+1)  # 왼쪽 서브 트리 먼저 출력
        ret += str(nodes[idx])+" "      # 루트노드 출력
        ret += inorder(nodes, idx*2+2)  # 오른쪽 서브 트리 출력
        return ret
    else:
        return ""
# print(inorder([1, 2, 3, 4, 5, 6, 7], 0))    
#4 2 5 1 6 3 7 

def postorder(nodes,idx):
    if idx < len(nodes):
        ret = postorder(nodes, idx*2+1)
        ret += postorder(nodes, idx*2+2)
        ret += str(nodes[idx]) + " "
        return ret
    else:
        return ""
# print(postorder([1, 2, 3, 4, 5, 6, 7], 0))   
# 4 5 2 6 7 3 1  
    
def solution(nodes):# (노드 리스트 & 루트 노드)의 인덱스를 매개변수로 각각 호출
    return [preorder(nodes,0,)[:-1],
            inorder(nodes,0)[:-1],
            postorder(nodes,0)[:-1]]   #마지막 공백 제거

print(solution([1,2,3,4,5,6,7]))
#['1 2 4 5 3 6 7', '4 2 5 1 6 3 7', '4 5 2 6 7 3 1']    
