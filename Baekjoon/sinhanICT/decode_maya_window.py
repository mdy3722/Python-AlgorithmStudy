# 개선된 마야 문자열 구하기
# 순열 전체를 생성하지 말고, w의 문자 빈도수만 기억해두고
# s의 부분 문자열과 문자 빈도수가 같은지 비교..

'''
counter 자료구조
문자열이나 리스트처럼 반복 가능한 객체에서 각 원소가 몇 번 나오는지 세어주는 자료구조
word = "cAda"
c = Counter(word)
print(c)

[출력 결과]
Counter({'a': 2, 'c': 1, 'A': 1})

Counter("Acad") == Counter("cadA")  # True -> 이렇게 순서를 고려하지 않고 문자 빈도만 비교!

주의!
c1 = Counter({'a': 0, 'b': 1, 'c': 1})
c2 = Counter({'b': 1, 'c': 1})

print(c1 == c2)  # False

슬라이싱 윈도우 기법
abcd
awsderfg 비교 -> s[0:4], s[1:5], s[2:6]...s[4:8]
8 - 4 = 4
반복은 8 - 4 + 1
'''
from collections import Counter

g = 4
len_s = 11
w = "cAda"
s = "AbrAcadAbRa"

# g, len_s = map(int, input().split())
# w = input()
# s = input()

def decode_maya_optimized(g, len_s, w, s):
  all_ways = 0
  w_counter = Counter(w)
  s_counter = Counter(s[:g])

  if w_counter == s_counter:
    all_ways += 1
    
  for i in range(1, len_s-g+1):
    prev_char = s[i - 1]    # 슬라이싱하면서 제거될 맨 앞 문자
    next_char = s[i - 1 + g]    # 슬라이싱하면서 추가될 다음 문자

    s_counter[prev_char] -= 1
    if s_counter[prev_char] == 0:
      del s_counter[prev_char]

    s_counter[next_char] += 1

    if w_counter == s_counter:
      all_ways += 1
 
  return all_ways

print(decode_maya_optimized(g, len_s, w, s))
