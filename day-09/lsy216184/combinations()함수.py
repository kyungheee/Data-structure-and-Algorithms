from itertools import combinations
from collections import Counter

str1="abc"
str2="cba"
menu=[]

menu += combinations(str1,2) #[('a', 'b'), ('a', 'c'), ('b', 'c')]
menu += combinations(str2,2)  #[('c', 'b'), ('c', 'a'), ('b', 'a')]
#combinations 함수 특징!! -> 입력 문자열의 순서를 유지한 채로 조합을 뽑는다!

counter = Counter(menu)
#  Counter({('a', 'b'): 1, ('a', 'c'): 1, 
            # ('b', 'c'): 1, ('c', 'b'): 1, 
            # ('c', 'a'): 1, ('b', 'a'): 1})

for c in counter.items():
    print(c)
    # (('a', 'b'), 1)
    # (('a', 'c'), 1)
    # (('b', 'c'), 1)
    # (('c', 'b'), 1)
    # (('c', 'a'), 1)
    # (('b', 'a'), 1)
