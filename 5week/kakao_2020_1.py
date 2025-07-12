'''
Q. 문자열 압축
문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현
간단한 예로 aabbaccc의 경우 2a2ba3c(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)와 같이 표현할 수 있는데,
이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다. 예를 들면, abcabcdede와 같은 문자열은 전혀 압축되지 않습니다.
어피치는 이러한 단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법을 찾아보려고 합니다.

예를 들어, ababcdcdababcdcd의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 2개 단위로 잘라서 압축한다면 2ab2cd2ab2cd로 표현할 수 있습니다.
다른 방법으로 8개 단위로 잘라서 압축한다면 2ababcdcd로 표현할 수 있으며, 이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다.

단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됨

압축할 문자열 input이 매개변수로 주어질 때 위에서 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여
표현한 문자열 중 가장 짧은 것의 길이를 return...

* 문자열의 길이는 1 이상 1,000 이하입니다.
* 문자열은 알파벳 소문자로만 이루어져 있습니다.
* 항상 앞부터 정해진 길이만큼 잘라야 한다.
'''

# "문자열의 길이는 1 이상 1,000 이하입니다." => N^2 = 1000000, 백만은 컴퓨터가 처리가능
# N^3은 부하 심함. => 여기서 생각할 수 있는 것 : O(N^2)까지는 괜찮겠구나.

# 모든 경우에서 가장 압축을 많이 시킨 문자열의 길이를 반환해야 합니다. => 모든 경우를 봐야겠습니다.
# 언제까지? 사실상 문자열 절반 단위 이후부터는 의미없다. 어차피 자르는 단위가 절반 이상이면 중복 압축 불가능이므로
# 문자열 길이가 24이므로 최대 12단위까지만! 만약 홀수 길이, 예를들어 25면 25//2 = 12
# 따라서 1부터 N//2까지만 쪼개자.
# for split_size in range(1, n // 2 + 1):

# "abcabcabcabcdededededede"
# 1개 단위 - abcabcabcabcdededededede
# input = "abcdef"
# n = len(input)
# for i in range(0, n, 1):
#     print(input[i])
# 2개 단위 - abcabcabcabc6de
# input = "abcdef"
# n = len(input)
# for i in range(0, n, 2):
#     print(input[i:i+2])   # 인덱스 범위 넘어가는 걱정에 대하여, 파이썬의 경우 인덱스 범위가 넘어가는 경우 알아서 처리해줌

# 3개 단위 - 4abcdededededede
# 4개 단위 - abcabcabcabc3dede
# 5개 단위 - abcabcabcabcdededededede
# 6개 단위 - 2abcabc2dedede
# 7개 단위 - ...

# 최종 자료구조
# input = "abcdef"
# n = len(input)
# for split_size in range(1, n//2+1):
#   splited_array =[input[i:i+split_size] for i in range(0, n, split_size)]

input = "abcabcabcabcdededededede"


def string_compression(string):
    n = len(string)
    result = n
    for split_size in range(1, n//2+1):      
        splited_array = [string[i:i+split_size] for i in range(0, n, split_size)]
        print(splited_array)

        compressed = ""   # 압축된 문자열
        count = 1
        for i in range(0, len(splited_array) - 1):   # 왜 len(splited_array) - 1인가? 앞을 기준으로 뒤와 같은지를 비교할 것이기 때문에.
            cur, next = splited_array[i], splited_array[i+1]

            if cur == next:
                count += 1
            else:
                if count == 1:
                    compressed += cur
                else:
                    compressed += f"{count}{cur}"
                count = 1    # 다음 비교를 위해 초기화

        if count == 1:
            compressed += splited_array[-1]
        else:
            compressed += f"{count}{splited_array[-1]}"
        print(compressed)    

        result = min(result, len(compressed))

    return result


print(string_compression(input))  # 14 가 출력되어야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))
