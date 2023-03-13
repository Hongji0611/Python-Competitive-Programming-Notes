# * 가변인자: 입력받은 값중 첫번째, 마지막 값을 제외
_list = [1, 2, 3, 4, 5]
first_index, *rest, last_index = _list
print(rest)

# * Unpacking
_list = [1, 2, 3, 4, 5]
print(*_list) # 1 2 3 4 5

# Packing
a, b, c = [1, 2, 3]
d = a, b, c
print(d) #(1, 2, 3)


#List Comprehension: 백준 1920번 "수 찾기" (http://boj.kr/1920)
import sys
input = sys.stdin.readline

# n = input()
# A = set(map(int, input().split()))
# m = input()
# _list = list(map(int, input().split()))

# print( *[1 if i in A else 0 for i in _list], sep='\n')

# 1 ~ 10을 담는 리스트
_list = [i for i in range(10)]
# 2, 4, 6, ..., 20을 담는 리스트
_list = [ i * 2 for i in range(10)]
# 주어진 리스트를 받아 3의 배수만 담는 리스트
import random
tmp = [random.randrange(1, 200) for _ in range(100)]
_list = [ i for i in tmp if i % 3 == 0]
# 값이 두개 들어있는 튜플을 받아 리스트를 생성하되, 튜플 내부의 값을 뒤집어서 저장하세요.
_tuple = [(i, j) for i in range(100) for j in range(100, 0, -1)]
_list = [(j, i) for (i, j) in _tuple]
print(tmp[1], _list[1])
# 주어진 리스트를 그대로 담되, 15가 넘어가는 값은 15로 바꿔서 저장합시다.
_changeList = [15 if i > 15 else i for i in tmp]
print(_changeList)
# 두 개의 리스트를 합치되, 가능한 모든 조합을 저장하는 리스트
x = [i for i in range(5)]
y = [i for i in range(5)]
_list = [ (i, j) for j in y for i in x]

# 앞쪽에 붙는 if는 삼항 연산자의 if라고 생각하시면 되고, (즉, 값이 앞 조건을 만족하면 어떤 값, 만족하지 못하면 다른 값) 맨 끝에 붙는 if는 값을 넣을지, 뺄지 결정하는 조건이라고 생각하시면 됩니다.

# 값을 찾기 위해 set 사용. set은 같은 값이 들어올 수 없음
i_want_to_erase_duplicate_element = [21, 31, 65, 21, 58, 94, 13, 31, 58]
completed_list = list(set(i_want_to_erase_duplicate_element)) # 21, 31, 65, 58, 94, 13

# dictionary 
fruit = ['apple', 'grape', 'orange', 'banana']
price = [3200, 15200, 9800, 5000]
_dict = dict(zip(fruit, price))
print(_dict)

# 딕셔너리에서 없는 값을 찾으려고 하면, 오류가 납니다. -> setdefault 사용
print(_dict.setdefault('strawberry', 0))
print(_dict)

# defaultdict
from collections import defaultdict

_int_dict = defaultdict(int)
print(_int_dict['apple'])
print(* _int_dict.keys())
print(* _int_dict.values())
print(* _int_dict.items())

#Sorting
#sort() 라는 메소드=> 리스트만 가능, sorted(컨테이너형데이터) 함수 => 리스트 반환
_list = [5, 6, 4, 8, 2, 3]
_set =  {65, 12, 15, 156, 31, 54, 94, 82, 31}
_list.sort()
print(_list)
print(sorted(_list))
print(sorted(_set))

#내림차순 정렬
print(sorted(_list, reverse = True))

#튜플의 리스트를 정렬하고 싶은데, 첫번째 값으로 오름차순 정렬을 하는데 값이 같으면 두번째 값으로 내림차순 정렬하고 싶어
_list = [(1, 3), (8, 2), (2, 5), (4, 7)]
sorted_list = sorted(_list, key = lambda dt: (dt[0], -dt[1]))
print(sorted_list)

#문자열 비교 (대소관계 상관 없이 정렬)
_list = ["CHicken", "hamburger", "Sushi", "chocolate"]

print(sorted(_list, key = lambda dt: dt.lower()))

#양 끝에 있는 문자열을 제거. 두개 이상의 문자열을 넣어주면, 두개를 모두 지워버립니다. and 조건이 아니라 or 조건이에요!
print('====chick*en*=====*'.strip('=*'))

#문자열 뒤집기 string[시작:종료(포함 안 함):간격]
string = 'I am Hungry...'
print(string[::-1])
print(reversed(string)) #메모리 주소 나옴
print("".join(reversed(string)))

#완전탐색(조합과 순열)
#1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열을 모두 구하시오.
import itertools
_list = [1, 2, 3, 4]
iter = itertools.combinations(_list, 2) #조합(중복 없음, 순서 구분X) 12 13 14 23 24 34
iter = itertools.permutations(_list, 2) #순열(중복 없음, 순서 O) 12 13 14 21 23 24 31 32 34 41 42 43
iter = itertools.combinations_with_replacement(_list, 2) #조합( 중복 있음, 순서구분 X)
iter = itertools.product(_list, repeat= 2) #모든 경우의 수

# 전체 리스트에서 3개를 추출하여 곱했을 때, 그 곱의 최댓값을 출력하는 프로그램을 작성하시오.
iter = itertools.combinations(_list, 3)
_list = [i[0] * i[1] * i[2] for i in iter]
_list.sort(reverse= True)
print(_list[0])

#sum
_list = [1, 2, 3, 4, 5]
print(sum(_list))

#join => 문자열로 되돌려줌
_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(', '.join(map(str, _list)))

#swap
a, b = 1, 2
a, b = b, a
print(a, b)

#Enumerate
_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for idx, val in enumerate(_list):
    print(idx, val)

#Counter
from collections import Counter
_list = Counter('hello world')
print(_list)
print(_list.most_common())
