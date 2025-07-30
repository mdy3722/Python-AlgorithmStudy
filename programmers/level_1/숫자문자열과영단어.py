'''
숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어짐
s가 의미하는 원래 숫자를 return하도록!!

접근 사고 과정
1. 문자열 안에 섞여있는 영단어를 숫자로 바꾼다? 즉 문자열을 새로운 문자열로 바꾼다.
2. 변환 대상이 명확하다. ex. "one"은 무조건 1, "two"는 무조건 2
  => 이를 통해 키-값 쌍이 존재하니까 딕셔너리를 생각할 수 있다.
3. 그럼 다시 1번 사고 과정으로 돌아가서, 문자열 안에 특정 단어를 다른 단어로 바꾸려면?
  str.replace(기존, 대체값) # 이때 주의할 것은 대체값의 타입은 string이다.
'''

'''
str.replace(old, new) : 문자열 전체를 왼쪽부터 오른쪽으로 순차적으로 스캔하면서 일치하는 old 문자열을 모두 new로 대체한다.
'''
s = "one4seveneight"

def solution(s):
    num_words = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5",
                 "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    
    for key, val in num_words.items():    # 딕셔너리 순회
        s = s.replace(key, val)

    return int(s)

print("정답은 1478입니다. 정답 : ", solution(s))