# 가장 효율적인 것은 알파벳을 인덱스화 하여 배열에 빈도수를 저장!
# ord('A') -> 65
# ord('a') -> 97
# chr(65) -> A
# 'B'는 ord('B') - ord('A')인 1, 즉 인덱스 1번째에 저장됨
# 만약 이 인덱스 1을 가지고 B를 반환하고자 한다면, 1 + ord('A') 를 chr에 넘겨주면 됨
# 즉 chr(인덱스 + ord('A'))
# 알파벳은 대문자 26개, 소문자 26개 총 52개가 있다.

w = "cAda"
s = "AbrAcadAbRa"
g = len(w)
len_s = len(s)

def to_index(c):
  if 'A' <= c <= 'Z':
    index = ord(c) - ord('A')
  else:
    index = 26 + ord(c) - ord('a')
  
  return index

def decode_maya(w, s):
  all_ways = 0 
  w_count = [0] * 52
  s_count = [0] * 52

  for ch in w:
    w_count[to_index(ch)] += 1

  for ch in s[:g]:
    s_count[to_index(ch)] += 1

  if w_count == s_count:
    all_ways += 1

  for i in range(1, len_s - g + 1):
    prev_char = s[i - 1]
    next_char = s[i - 1 + g]

    s_count[to_index(prev_char)] -= 1
    s_count[to_index(next_char)] += 1

    if s_count == w_count:
      all_ways += 1

  return all_ways

print(decode_maya(w, s))
