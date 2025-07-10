'''
상근이는 카드 n(4 ≤ n ≤ 10)장을 바닥에 나란히 놓고 놀고있다.
각 카드에는 1이상 99이하의 정수가 적혀져 있다. 상근이는 이 카드 중에서 k(2 ≤ k ≤ 4)장을 선택하고, 가로로 나란히 정수를 만들기로 했다.
상근이가 만들 수 있는 정수는 모두 몇 가지일까?

예를 들어, 카드가 5장 있고, 카드에 쓰여 있는 수가 1, 2, 3, 13, 21라고 하자.
여기서 3장을 선택해서 정수를 만들려고 한다. 2, 1, 13을 순서대로 나열하면 정수 2113을 만들 수 있다. 또, 21, 1, 3을 순서대로 나열하면 2113을 만들 수 있다.
이렇게 한 정수를 만드는 조합이 여러 가지 일 수 있다.
n장의 카드에 적힌 숫자가 주어졌을 때, 그 중에서 k개를 선택해서 만들 수 있는 정수의 개수를 구하는 프로그램을 작성하시오.
'''

# 1. 카드의 순서가 중요 -> 순열
# 2. 이미 만들어진 숫자는 또 계산할 필요가 없다. 중복을 제거해서 집어넣자. -> set
# 3. set의 길이를 출력
# 순열 vs 조합 vs 중복조합
# 순열 - 순서 중요, 중복 안됨
# 조합 - 순서 무시, 중복 안됨 -> 뽑는 거, 근데 AB를 뽑나 BA를 뽑나 같은 것으로 판단
# 중복 조합 - 순서 무시, 중복 허용 -> 뽑는데, 뽑았던 거 또 뽑아도 됨.

# arr = ['A', 'B', 'C']

# print(list(permutations(arr, 2)))  # 순열
# print(list(combinations(arr, 2)))  # 조합
# print(list(combinations_with_replacement(arr, 2)))  # 중복 조합

from itertools import permutations     # 순열

n = 4
k = 2
card = [1, 2, 12, 1]


def get_all_ways_card(n, k, card):
  numbers = set()   # 중복 정수값 방지
                    # set은 append가 아닌 add를 씁니다. -> numbers.add(p)
  for p in permutations(card, k):       # permutations(cards, k)는 순열 경우들을 튜플로 반환
    num = ''.join(map(str, p))          # ''.join(p) -> 리스트나 튜플 p 안에 있는 문자열들을 공백 없이 합침 ex. ["1", "2"] => "12"
                                        # 주의할 점은 문자열만 가능! -> 만약 입력값이 정수인 경우 str로 변환 필요
                                        # 보통은 number = ''.join(map(str, p)) 와 같이 map(str, p)을 사용하여 리스트 안의 타입을 str로 변환하여 합침
    numbers.add(num)    # set이므로 같은 정수면 추가 안함
  
  all_ways = len(numbers)

  return all_ways

print(get_all_ways_card(n, k, card))
print(get_all_ways_card(6, 3, [72, 2, 12, 7, 2, 1]))




# 아래는 입력을 개행 단위로 받는 경우의 코드
# from itertools import permutations

# n = int(input())
# k = int(input())
# cards = [input().strip() for _ in range(n)]

# numbers = set()

# for p in permutations(cards, k):
#     number = ''.join(p)  # 정수들을 문자열로 바꿔서 붙이기
#     numbers.add(number)

# print(len(numbers))
