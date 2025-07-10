"""
고고학자들은 W라는 특정 단어를 발굴 기록으로부터 찾고 있다.
그 단어를 구성하는 각 글자들은 무엇인지를 알고 있지만
이것이 고대 기록에 어떤 형태로 숨어 있는지는 다 알지 못한다.
W를 이루고 있는 g개의 그림문자와, 연구 대상인 벽화에 기록된 마야 문자열 S가 주어졌을 때,
단어 W가 마야 문자열 S에 들어있을 수 있는 모든 가짓수를 계산하는 프로그램을 작성하시오.

즉 문자열 S안에서 문자열 W의 순열 중 하나가 부분 문자열로 들어있는 모든 경우의 수를 계산하라는 뜻이다.

[입력]
첫 줄에 고고학자들이 찾고자 하는 단어 W의 길이 g와 발굴된 벽화에서 추출한 문자열 S의 길이 |S|가
빈 칸을 사이에 두고 주어진다. (1<=g<=3,000, g<=|S|<=3,000,000)
둘째 줄에 W, 셋째 줄에 S의 실제 내용이 들어있다.
모든 문자열은 알파벳으로 이루어지며, 대소문자를 구분한다.

[출력]
첫째 줄에 W의 순열이 S 안에 있을 수 있는 형태의 개수를 출력한다.

예시
[입력]
4 11
cAda
AbrAcadAbRa

[출력]
2
Acad와 cadA

s문자열을 인덱스 0부터 w의 길이만큼 끊어서 perms_of_w에 있는지 보자.
문자열 슬라이싱 - string[시작:끝+1]
시작~끝까지 => w 길이,,, 여기서는 4
길이가 11인 s문자열의 마지막 인덱스는 10이다. 
예를들어 s문자열 처음부터 w길이만큼 끊어라. => s[0:4], s[1:5], ... , s[7:11]

위를 통해 다음 내용을 정리할 수 있다.
인덱스를 0부터 7까지 반복..총 8번 이때 7은 11-4이고 이는 len(s)-g
슬라이싱은 s[i:i+g]
"""
from itertools import permutations

# g, len_s = int(input().split()) -> 이러면 안됨. input().split()은 기본적으로 리스트를 반환함
# g, len_s = map(int, input().split())으로 수정해야..
# w = input()
# s = input()

g = 4
len_s = 11
w = "cAda"
s = "AbrAcadAbRa"

def decode_maya(g, len_s, w, s):
  all_ways = 0

  perms_of_w = set()

  for p in permutations(w):     # w의 순열들이 ("c", "d", "a", "A") 형태로 반환
    perm = ''.join(p)           # cdaA
    perms_of_w.add(perm)

  count_of_word = len_s - g + 1
  for i in range(count_of_word):
    word = s[i:i+g]

    if word in perms_of_w:
      all_ways += 1

  return all_ways

print(decode_maya(g, len_s, w, s))

# 위 풀이는 내가 짠 코드로, 순열을 이용한 풀이. 이때 w는 g만큼의 길이를 갖고 있는데
# 이는 최대 3000이고 순열 가짓수는 최대 3000! 만큼이므로 메모리 초과 가능성..