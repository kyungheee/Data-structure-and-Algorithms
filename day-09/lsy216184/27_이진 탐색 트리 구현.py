# 1. 노드 클래스 정의 (이진 탐색 트리에 사용할 노드 생성)
class Node:

# 2. 노드 클래스 생성자
    def __init__ (self, key):   #self=자기 자신을 참조  / #key=노드가 저장할 값을 받음
        self.left = None    #초기에는 어떤 자식노드도 연결되어있지 않기 때문에 왼/오 노드 none으로 설정됨
        self.right = None
        self.val = key

# 3. 이진 탐색 트리 클래스
class BST:
    # 4. 루트노드를 none으로 초기화 /초기에는 아무것도 없음
    def __init__(self):       
        self.root = None
    
    #5. 루트노드 부터 시작해서 " 이진탐색 트리 규칙"에 맞는 위치에 새 노드 삽입
    def insert(self, key):         
        if not self.root:          # 루트노드 없으면 삽입
            self.root = Node(key)
        else:
            curr = self.root       #루트노드 있다면 크기확인 해서 왼/오 보내기
            while True:
                if key < curr.val:          # 삽입값 < 현재노드 값
                    if curr.left:           # 왼쪽 노드 있나?
                        curr = curr.left    # 있다면 왼쪽 자식 노드로 이동
                    else:
                        curr.left=Node(key)    #없으면 새노드 생성
                        break

                else:                       # 삽입값 > 현재노드 값
                    if curr.right:          # 오른쪽 노드 있나?
                        curr = curr.right   # 있다면 왼쪽 자식 노드로 이동
                    else:                   
                        curr.right = Node(key)    #없으면 새노드 생성
                        break
        
    #6. 이진 탐색 규칙에 따라 특정값 key있는지 확인
    def search(self,key): 
        curr = self.root                  # 루트노드부터 시작
        while curr and curr.val != key:   # 현재노드 존재 확인 and 현재노드 값, 찾는 값 다르면 반복
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr
    
# 7. lst데이터를 활용해 이진탐색트리 생성, search_lst 원소 탐색    
def solution(lst, search_lst):   
    bst = BST()                  # BST함수를 bst로 부른다
    for key in lst:              # lst의 각 요소 = key
        bst.insert(key)          # bst함수에 key 대입
    result=[]

    for search_val in search_lst:     # 검색lst의 각 요소는 이진탐색트리에서 검색하고
        if bst.search(search_val):    # bst함수에 찾을값 대입
            result.append(True)       # 있으면(T), 없으면(F) 결과 리스트에 추가
        else:
            result.append(False)
    return result

print(solution([5,3,8,4,2,1,7,10],[1,2,5,6]))
print(solution([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))

# [True, True, True, False]
# [False, False, False, False, False]
                    
                
