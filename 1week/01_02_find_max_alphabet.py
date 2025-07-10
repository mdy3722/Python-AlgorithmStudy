def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t", "u", "v", "x", "y", "z"]
    max_occurrence = 0
    max_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:
        occurence = 0
        for char in string:
            if char == alphabet:
                occurence += 1
        if occurence > max_occurrence:
            max_alphabet = alphabet
            max_occurrence = occurence

    return max_alphabet


# 알파벳 별로 빈도수를 리스트에 저장 => 효율적인 자료구조가 배열
# 0번째 - a, 1번째 - b .....
# 문자를 아스키 코드로 변형하는 법은 ord(문자)로..
# ord('a')-97 = 0, 반대로 chr(97)을 하면 a가 반환
# d를 배열에 담고 싶다? 몇번째 인덱스로..? ord('d')-ord('a')
def find_alphabet_occurrence_array(string):
    alphabet_occurrences_array = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
        index = ord(char) - ord('a')
        alphabet_occurrences_array[index] += 1

    max_occurrence = 0
    max_alphabet_index = 0

    for i in range(len(alphabet_occurrences_array)):
        occurence = alphabet_occurrences_array[i]
        if occurence > max_occurrence:
            max_occurrence = occurence
            max_alphabet_index = i

    max_occurred_char = chr(ord('a') + max_alphabet_index)
    return max_occurred_char




result = find_alphabet_occurrence_array
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))