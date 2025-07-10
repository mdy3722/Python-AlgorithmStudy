'''
온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어짐.
이때 회원들은 나이가 증가하는 순으로,, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하시오.

입력
첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)
둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다.
나이는 1보다 크거나 같으며, 200보다 작거나 같은 정수이고, 이름은 알파벳 대소문자로 이루어져 있고, 길이가 100보다 작거나 같은 문자열이다.
입력은 가입한 순서로 주어진다.

출력
첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순으로
한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.
'''

# 파이썬에서 sorted()와 .sort()는 stable sort로 정렬 기준 값이 같은 경우, 원래 순서가 유지되는 정렬이다.
# 지금처럼 입력값 n이 100000 가까이 될 때는 input() 보다는 sys.stdin.readline을 쓰는 것이 시간을 단축한다.
'''백준'''
# import sys

# n = int(sys.stdin.readline())
# members = []

# for _ in range(n):
#   age, name = sys.stdin.readline().split()
#   members.append([int(age), name])

# members.sort(key=lambda x: x[0])    # age 기준, .sort()는 stable sort라 age 같으면 입력 순서로 정렬

# for age, name in members:
#   print(age, name)

'''def solution(n) 버전'''
n = 3
members = [
    [21, "Junkyu"],
    [21, "Dohyun"],
    [20, "Sunyoung"]
]

def sort_by_age(n, members):
  members.sort(key=lambda x: x[0])


  for age, name in members:
    print(age, name)

sort_by_age(n, members)




# 동적으로 입력을 받을 때마다 정렬이 필요, 나이가 증가되는 순으로 -> heap
# 근데 이때 나이가 같으면 먼저 들어온 순서로,,

'''힙 방식'''
import heapq

members = [(21, "Junkyu"), (21, "Dohyun"), (20, "Sunyoung")]

heap = []

def get_sort_by_age(members, heap):
  order = 0
  for age, name in members:
    heapq.heappush(heap, (age, order, name))        # age가 같으면 order, order이 같으면 name 순으로 자동 정렬
    order += 1

  while heap:
    age, _, name = heapq.heappop(heap)
    print(age, name)

get_sort_by_age(members, heap)

