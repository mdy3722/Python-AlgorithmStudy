input = "abadabac"

# 풀지 못함
def find_not_repeating_first_character(string):
    # 이 부분을 채워보세요!
    # 반복되는지 아닌지를 판단해야 함. 이전 과제를 참고하여 알파벳의 개수가 한 개인 것을 구하면 되지 않을까
    # 근데 이 경우 첫 알파벳이 c인지 d인지 알 수 없음 -> 다시 한 번 반복을 통해 누가 먼저 나왔는지를 체크해야...
    # 결론 : 빈도수를 찾고 빈도수가 1인 알파벳들 중에서 string에서 먼저 뭐가 나왔는지를 ,,
    occurence_Array = find_alphabet_occurrence_array(string)
    not_repeating_character_Array = []
    for index in range(len(occurence_Array)):   # O(1)
        alphabet_occurence = occurence_Array[index]
        if alphabet_occurence == 1:
            not_repeating_character_Array.append(chr(ord('a')+index))
    for char in string:
        if char in not_repeating_character_Array:
            return char
    return "_"


def find_alphabet_occurrence_array(string):
    alphabet_occurrences_array = [0] * 26
    for char in string:     # N의 시간복잡도
        if not char.isalpha():
            continue
        index = ord(char) - ord('a')
        alphabet_occurrences_array[index] += 1

    return alphabet_occurrences_array

# 최종적으로 O(N)만큼 걸리는 함수

result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))